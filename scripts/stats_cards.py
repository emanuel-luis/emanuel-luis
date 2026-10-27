"""Render the profile's GitHub stats cards as static SVGs (no third-party service at read time).

Usage:
    GITHUB_TOKEN=... python3 scripts/stats_cards.py --login emanuel-luis --out assets
    python3 scripts/stats_cards.py --self-test

Public data only: the workflow's GITHUB_TOKEN cannot see private repositories.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path
from xml.etree import ElementTree
from xml.sax.saxutils import escape

API = "https://api.github.com/graphql"
QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    name
    login
    pullRequests { totalCount }
    issues { totalCount }
    repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST, ISSUE]) { totalCount }
    contributionsCollection { contributionCalendar { totalContributions } }
    repositories(first: 100, after: $after, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 20, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

# tokyonight, the theme the README used before.
BG, TITLE, TEXT, MUTED = "#1a1b27", "#70a5fd", "#38bdae", "#a9b1d6"
FONT = "font-family:'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif"


def graphql(token: str, login: str, after: str | None) -> dict:
    body = json.dumps({"query": QUERY, "variables": {"login": login, "after": after}}).encode()
    request = urllib.request.Request(
        API,
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors"):
        raise RuntimeError(f"GraphQL errors: {payload['errors']}")
    return payload["data"]["user"]


def fetch(token: str, login: str) -> dict:
    """Return the user's totals plus every public, non-fork repo it owns (paginated)."""
    user = graphql(token, login, None)
    repos = list(user["repositories"]["nodes"])
    page = user["repositories"]["pageInfo"]
    while page["hasNextPage"]:
        more = graphql(token, login, page["endCursor"])["repositories"]
        repos += more["nodes"]
        page = more["pageInfo"]
    user["repositories"]["nodes"] = repos
    return user


def summarize(user: dict) -> tuple[list[tuple[str, int]], list[tuple[str, str, float]]]:
    """Stats rows and the top 8 languages by bytes, as (name, color, percent)."""
    repos = user["repositories"]["nodes"]
    rows = [
        ("Total stars", sum(r["stargazerCount"] for r in repos)),
        ("Contributions (last year)",
         user["contributionsCollection"]["contributionCalendar"]["totalContributions"]),
        ("Pull requests", user["pullRequests"]["totalCount"]),
        ("Issues", user["issues"]["totalCount"]),
        ("Contributed to (external repos)", user["repositoriesContributedTo"]["totalCount"]),
        ("Public repositories", user["repositories"]["totalCount"]),
    ]
    sizes: dict[str, int] = {}
    colors: dict[str, str] = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            sizes[name] = sizes.get(name, 0) + edge["size"]
            colors[name] = edge["node"]["color"] or MUTED
    top = sorted(sizes.items(), key=lambda item: item[1], reverse=True)[:8]
    total = sum(size for _, size in top) or 1
    langs = [(name, colors[name], 100 * size / total) for name, size in top]
    return rows, langs


def card(width: int, height: int, title: str, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">'
        f"<title>{escape(title)}</title>"
        f'<rect width="{width}" height="{height}" rx="4.5" fill="{BG}"/>'
        f'<text x="25" y="35" fill="{TITLE}" style="{FONT};font-size:18px;font-weight:600">'
        f"{escape(title)}</text>{body}</svg>\n"
    )


def render_stats(name: str, rows: list[tuple[str, int]]) -> str:
    lines = []
    for i, (label, value) in enumerate(rows):
        y = 70 + i * 22
        lines.append(
            f'<text x="25" y="{y}" fill="{TEXT}" style="{FONT};font-size:14px;font-weight:600">'
            f"{escape(label)}:</text>"
            f'<text x="300" y="{y}" fill="{TEXT}" style="{FONT};font-size:14px;font-weight:700">'
            f"{value:,}</text>"
        )
    height = 70 + len(rows) * 22
    return card(495, height, f"{name}'s GitHub stats", "".join(lines))


def render_langs(langs: list[tuple[str, str, float]]) -> str:
    bar, legend, x = [], [], 25.0
    for i, (name, color, percent) in enumerate(langs):
        width = 300 * percent / 100
        bar.append(f'<rect x="{x:.2f}" y="55" width="{width:.2f}" height="8" fill="{color}"/>')
        x += width
        col, row = i % 2, i // 2
        lx, ly = 25 + col * 160, 90 + row * 24
        legend.append(
            f'<circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{color}"/>'
            f'<text x="{lx + 15}" y="{ly}" fill="{MUTED}" style="{FONT};font-size:12px">'
            f"{escape(name)} {percent:.1f}%</text>"
        )
    height = 90 + ((len(langs) + 1) // 2) * 24
    return card(350, height, "Most used languages", "".join(bar + legend))


SAMPLE = {
    "name": "Ana <Test>",
    "login": "ana",
    "pullRequests": {"totalCount": 12},
    "issues": {"totalCount": 3},
    "repositoriesContributedTo": {"totalCount": 2},
    "contributionsCollection": {"contributionCalendar": {"totalContributions": 1234}},
    "repositories": {
        "totalCount": 2,
        "nodes": [
            {"stargazerCount": 5, "languages": {"edges": [
                {"size": 600, "node": {"name": "Python", "color": "#3572A5"}},
                {"size": 100, "node": {"name": "C#", "color": None}},
            ]}},
            {"stargazerCount": 2, "languages": {"edges": [
                {"size": 300, "node": {"name": "Python", "color": "#3572A5"}},
            ]}},
        ],
    },
}


def self_test() -> None:
    rows, langs = summarize(SAMPLE)
    assert dict(rows)["Total stars"] == 7
    assert dict(rows)["Contributions (last year)"] == 1234
    assert [name for name, _, _ in langs] == ["Python", "C#"]
    assert abs(sum(p for _, _, p in langs) - 100) < 1e-9
    assert langs[1][1] == MUTED  # a language without a color falls back
    for svg in (render_stats(SAMPLE["name"], rows), render_langs(langs)):
        ElementTree.fromstring(svg)  # well-formed XML, names escaped
    assert "Ana &lt;Test&gt;" in render_stats(SAMPLE["name"], rows)
    print("self-test ok")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the profile's GitHub stats cards.")
    parser.add_argument("--login")
    parser.add_argument("--out", type=Path, default=Path("assets"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    token = os.environ.get("GITHUB_TOKEN")
    if not args.login or not token:
        parser.error("--login and the GITHUB_TOKEN environment variable are required")
    user = fetch(token, args.login)
    rows, langs = summarize(user)
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "stats.svg").write_text(render_stats(user["name"] or user["login"], rows), "utf-8")
    (args.out / "top-langs.svg").write_text(render_langs(langs), "utf-8")
    print(f"wrote {args.out / 'stats.svg'} and {args.out / 'top-langs.svg'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
