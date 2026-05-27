
<h1 align="center">Emanuel Luis</h1>

<p align="center">
  <strong>Data Engineer</strong> · batch &amp; CDC ingestion · dbt modeling · orchestration · data platforms
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/emanuel-luis-/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://stackoverflow.com/users/17576381/tiov4d3r"><img src="https://img.shields.io/badge/Stack_Overflow-F58025?style=flat&logo=stackoverflow&logoColor=white" alt="Stack Overflow"></a>
  <a href="mailto:emanuel.filho08@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=flat&logo=gmail&logoColor=white" alt="Email"></a>
</p>

---

### About

I design and build **scalable data pipelines and modern data architectures** that enable organizations
to extract strategic value from data. **3+ years** in data engineering on a strong software-engineering
foundation — specializing in **ETL/ELT**, **data lakes**, and **analytics platforms**.

Data Engineer at **PULSE**, the data department of **Grupo Mateus** (São Luís, Brazil); B.S. in
Software Engineering from **UNDB**.

**Core expertise**
- **Data pipeline engineering** — ETL/ELT design, ingestion, and transformation at scale
- **Data architecture** — data lakes, data warehouses, the modern data stack
- **Cloud** — Azure (Data Factory, Data Lake, Blob Storage) · Databricks
- **Stack** — Python, PySpark, SQL, dbt, Airflow
- **Data modeling** — analytics engineering, dimensional modeling

*Interests: data platform engineering, modern data stack, distributed data processing, data governance.*

### Experience

<!-- IP-safe (no internal names). Metric is from your LinkedIn — adjust if needed. -->
**Data Engineer — PULSE** (data department @ **Grupo Mateus**) · Aug 2022 – present
- Design and maintain **scalable data pipelines processing millions of records daily** across 20+ source systems (**700+ ingestion configs**, **~90 dbt DAGs**).
- Built a **data lakehouse** on **Azure + Databricks** — medallion architecture (staging → bronze → gold) with **Delta Lake** and **Unity Catalog**.
- Built a **materialized change-tracking (CDC) system** that cut a key pipeline's runtime from **~60 min to 13 min**.
- Engineered batch / incremental / **CDC** ingestion (MSSQL, PostgreSQL) standardized via config-driven **Airflow** DAG generators and a shared **PySpark extraction library** (fullscan, incremental, CDC, Autoloader).
- Built curated **dbt** layers (bronze → staging → intermediate → marts) orchestrated by **Astronomer Cosmos** (dbt-in-Airflow).
- Tuned **Spark/PySpark** on Databricks (Liquid Clustering, broadcast joins), wrote **Protobuf** messages to **Confluent Kafka**, and ran **Reverse ETL** via Apache NiFi.
- Built metadata-driven DAG generation system (**Jinja2 templates** + JSON/YAML configs → auto-rendered Airflow DAGs).
- Authored **`pylakeutils`** — a shared Python library for extraction/loading patterns (RDBMS, CDC, Autoloader), deployed as wheels to Databricks.
- Ran containerized workloads on **Azure Container Instances** (ACI) with **Docker** images hosted on **Azure Container Registry** (ACR).

### Tech

**Languages & processing**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Polars](https://img.shields.io/badge/Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![PyArrow](https://img.shields.io/badge/PyArrow-E25A1C?style=for-the-badge&logo=apache&logoColor=white)

**Data engineering & orchestration**

![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Astronomer Cosmos](https://img.shields.io/badge/Astronomer_Cosmos-4E2A8E?style=for-the-badge&logo=astronomer&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Delta Lake](https://img.shields.io/badge/Delta_Lake-003366?style=for-the-badge&logo=delta&logoColor=white)
![Delta Live Tables](https://img.shields.io/badge/Delta_Live_Tables-003366?style=for-the-badge&logo=databricks&logoColor=white)
![Protobuf](https://img.shields.io/badge/Protobuf-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Apache NiFi](https://img.shields.io/badge/NiFi-728E9B?style=for-the-badge)

**Platforms & cloud**

![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)
![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
![Confluent Cloud](https://img.shields.io/badge/Confluent-231F20?style=for-the-badge&logo=apachekafka&logoColor=white)
![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-FF3621?style=for-the-badge&logo=databricks&logoColor=white)

**Data stores**

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Trino](https://img.shields.io/badge/Trino-DD00A1?style=for-the-badge&logo=trino&logoColor=white)
![Cassandra](https://img.shields.io/badge/Cassandra-1287B1?style=for-the-badge&logo=apachecassandra&logoColor=white)
![ADLS Gen2](https://img.shields.io/badge/ADLS_Gen2-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)

**DevOps & tooling**

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844FBA?style=for-the-badge&logo=terraform&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Azure Pipelines](https://img.shields.io/badge/Azure_Pipelines-2560E0?style=for-the-badge&logo=azurepipelines&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

**Frameworks & libraries**

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)

### Featured projects

<!--
  TODO once built (see ../04-new-projects.md):
  - de-lakehouse-pipeline  — flagship end-to-end ELT (ingest -> dbt medallion -> marts -> dashboard)
  - ingestion-toolkit      — CLI generating Airflow ingestion DAGs (fullscan / incremental / CDC)
  Add them at the top of this list and pin them on the profile.
-->

| Project | What it shows |
| --- | --- |
| [`controladoria-api`](https://github.com/tiovader/controladoria-api) | Data/document platform — FastAPI (clean architecture), S3, Alembic migrations, Terraform, scheduled batch sync, Prometheus metrics. |
| [`vaccine-backend`](https://github.com/tiovader/vaccine-backend) | Dimensional modeling — star schema (dimension/fact), SQL DDL, and seed generation. |
| [`bank-credit`](https://github.com/tiovader/bank-credit) | Full-stack data app — FastAPI + React, graph-based routing and SLAs, migrations and tests. |
| [`ecommerce-scrapping`](https://github.com/tiovader/ecommerce-scrapping) | Data ingestion — Scrapy + Splash + Selenium with JavaScript rendering. |

### Open-source contributions

**[Astronomer Cosmos](https://github.com/astronomer/astronomer-cosmos)** — the dbt + Airflow integration library (1.6k+ stars). Two merged PRs:

| PR | What it fixed | Impact |
| --- | --- | --- |
| [#2201](https://github.com/astronomer/astronomer-cosmos/pull/2201) — `template_fields` in `DbtConsumerWatcherSensor` | Watcher-mode sensors crashed on fallback to local execution because templated fields from `DbtRunLocalOperator` were missing. Added the parent's `template_fields` to the sensor, with tests. | Unblocked users running Cosmos Watcher mode with fallback — any Cosmos user hitting #2193. |
| [#2241](https://github.com/astronomer/astronomer-cosmos/pull/2241) — Restore plain-text output in `ExecutionMode.WATCHER` | JSON log output introduced in a prior release made Airflow task logs unreadable in Watcher mode. Refactored `FullOutputSubprocessHook` to delegate logging through a `process_log_line` callable; made JSON format conditional on `SUBPROCESS` invocation mode only. | Restored readable dbt logs (with CLI colors) for Watcher-mode users while preserving real-time status tracking for Subprocess mode. 5 files, clean refactor reviewed and approved by Astronomer maintainers. |

### Certifications

- **Databricks Academy Accreditation — Databricks Fundamentals** · Databricks · May 2026
- **Computer Vision Training** · Data Inception · May 2022
- **Machine Learning Training** · Data Inception · Mar 2022

### Publications

- **Computational methodologies for detection & diagnosis of SARS-CoV-2 (COVID-19) from medical images** — ERCEMAPI (Regional Computing School, CE/MA/PI). <!-- confirm exact title, authors, year --> · code: [`PROJETO-DE-PESQUISA-COVID-19`](https://github.com/tiovader/PROJETO-DE-PESQUISA-COVID-19)

### GitHub

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=tiovader&show_icons=true&hide_border=true&count_private=true&theme=default" alt="stats" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=tiovader&layout=compact&hide_border=true&theme=default" alt="top languages" />
</p>

<details>
<summary>Education &amp; training</summary>

- **B.S. Software Engineering** — UNDB (Unidade de Ensino Superior Dom Bosco), São Luís, Brazil · 2021–2025
- Python and C# coursework — Udemy

(Professional certifications listed in the **Certifications** section above.)

</details>

<!--
  🇧🇷 Optional Portuguese version: keep this English-first README, or maintain a
  README.pt-BR.md and link it here. See ../05-readme-standards.md (Conventions).
-->
