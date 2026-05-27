
<h1 align="center">Emanuel Luis</h1>

<p align="center">
  <strong>Data Engineer</strong> · ingestion · dbt modeling · orchestration · data platforms
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

<table>
  <tr>
    <td><b>Languages &amp; processing</b></td>
    <td>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="30" alt="Python" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachespark/apachespark-original.svg" height="30" alt="PySpark" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azuresqldatabase/azuresqldatabase-original.svg" height="30" alt="SQL" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="30" alt="Pandas" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="30" alt="NumPy" />
      <img src="https://img.shields.io/badge/Polars-CD792C?style=flat&logo=polars&logoColor=white" height="22" alt="Polars" />
      <img src="https://img.shields.io/badge/PyArrow-E25A1C?style=flat&logo=apache&logoColor=white" height="22" alt="PyArrow" />
    </td>
  </tr>
  <tr>
    <td><b>Data engineering &amp; orchestration</b></td>
    <td>
      <img src="https://img.shields.io/badge/dbt-FF694B?style=flat&logo=dbt&logoColor=white" height="22" alt="dbt" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apacheairflow/apacheairflow-original.svg" height="30" alt="Airflow" />
      <img src="https://img.shields.io/badge/Astronomer_Cosmos-4E2A8E?style=flat&logo=astronomer&logoColor=white" height="22" alt="Cosmos" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/apachekafka/apachekafka-original.svg" height="30" alt="Kafka" />
      <img src="https://img.shields.io/badge/Delta_Lake-003366?style=flat&logo=delta&logoColor=white" height="22" alt="Delta Lake" />
      <img src="https://img.shields.io/badge/DLT-003366?style=flat&logo=databricks&logoColor=white" height="22" alt="Delta Live Tables" />
      <img src="https://img.shields.io/badge/Protobuf-4285F4?style=flat&logo=google&logoColor=white" height="22" alt="Protobuf" />
      <img src="https://img.shields.io/badge/NiFi-728E9B?style=flat" height="22" alt="NiFi" />
    </td>
  </tr>
  <tr>
    <td><b>Platforms &amp; cloud</b></td>
    <td>
      <img src="https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white" height="22" alt="Databricks" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg" height="30" alt="Azure" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="30" alt="GCP" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" height="30" alt="AWS" />
      <img src="https://img.shields.io/badge/Confluent_Cloud-231F20?style=flat&logo=apachekafka&logoColor=white" height="22" alt="Confluent" />
      <img src="https://img.shields.io/badge/Unity_Catalog-FF3621?style=flat&logo=databricks&logoColor=white" height="22" alt="Unity Catalog" />
    </td>
  </tr>
  <tr>
    <td><b>Data stores</b></td>
    <td>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" height="30" alt="PostgreSQL" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-original.svg" height="30" alt="SQL Server" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" height="30" alt="MongoDB" />
      <img src="https://img.shields.io/badge/Trino-DD00A1?style=flat&logo=trino&logoColor=white" height="22" alt="Trino" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cassandra/cassandra-original.svg" height="30" alt="Cassandra" />
      <img src="https://img.shields.io/badge/ADLS_Gen2-0078D4?style=flat&logo=microsoftazure&logoColor=white" height="22" alt="Azure Data Lake" />
      <img src="https://img.shields.io/badge/Azure_Blob-0078D4?style=flat&logo=microsoftazure&logoColor=white" height="22" alt="Azure Blob" />
    </td>
  </tr>
  <tr>
    <td><b>DevOps &amp; tooling</b></td>
    <td>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" height="30" alt="Docker" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/terraform/terraform-original.svg" height="30" alt="Terraform" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="30" alt="Git" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/githubactions/githubactions-original.svg" height="30" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/Azure_Pipelines-2560E0?style=flat&logo=azurepipelines&logoColor=white" height="22" alt="Azure Pipelines" />
      <img src="https://img.shields.io/badge/Azure_ACI-0078D4?style=flat&logo=microsoftazure&logoColor=white" height="22" alt="ACI" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" height="30" alt="Linux" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg" height="30" alt="Bash" />
    </td>
  </tr>
  <tr>
    <td><b>Frameworks &amp; libraries</b></td>
    <td>
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="30" alt="FastAPI" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" height="30" alt="SQLAlchemy" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" height="30" alt="Selenium" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pydantic/pydantic-original.svg" height="30" alt="Pydantic" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytest/pytest-original.svg" height="30" alt="pytest" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jinja/jinja-original.svg" height="30" alt="Jinja2" />
      <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/opencv/opencv-original.svg" height="30" alt="OpenCV" />
    </td>
  </tr>
</table>

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
