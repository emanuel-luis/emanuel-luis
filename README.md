
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

I'm a data engineer at PULSE, the IT department of Grupo Mateus in São Luís, Brazil, where I have
worked since August 2022. Most of my work is batch and CDC ingestion, dbt models on a Databricks
lakehouse, and the Airflow orchestration that runs them. I hold a B.S. in Software Engineering from
UNDB.

### Experience

**Data Engineer, PULSE** (IT department of Grupo Mateus) · Aug 2022 to present

- Design and maintain data pipelines that process millions of records a day from 20+ source
  systems: 700+ ingestion configs and about 90 dbt DAGs.
- Built a lakehouse on Azure and Databricks with a medallion layout (staging, bronze, gold) on
  Delta Lake and Unity Catalog.
- Cut one pipeline's runtime from about 60 minutes to 13 with a materialized change-tracking (CDC)
  system.
- Standardized batch, incremental and CDC ingestion from SQL Server and PostgreSQL with
  metadata-driven DAG generation: Jinja2 templates and JSON/YAML configs render the Airflow DAGs.
- Wrote a shared PySpark library for extraction and loading (full scan, incremental, CDC, Auto
  Loader), deployed to Databricks as wheels.
- Modeled dbt layers (bronze, staging, intermediate, marts) that run in Airflow through Astronomer
  Cosmos.
- Tuned Spark on Databricks (Liquid Clustering, broadcast joins), published Protobuf messages to
  Confluent Kafka, and ran reverse ETL with Apache NiFi.
- Ran containerized jobs on Azure Container Instances, with Docker images in Azure Container
  Registry.

**Data Engineer, payments fintech** (financial lakehouse, remote) · Apr 2026 to Sep 2026

- Root-caused a decimal-inference overflow in the MongoDB Spark connector that turned large
  financial values into NULL while the jobs reported success. Built the repair pipeline: a string
  copy of each decimal written at ingestion flags the values that came back NULL, those records
  are re-extracted in batches and merged back idempotently, and the fix propagates into silver and
  gold. A later recurrence exposed a second defect, a nulled fee component coalesced to zero:
  R$ 31,632.55 under-reported across 183 orders, invisible to NULL-based quality checks.
- Fixed a central-bank regulatory report that had dropped 22,408 transactions since two
  transaction types were introduced. Simulated the impact against the live regulatory table in
  staging and shipped the fix with a materiality threshold agreed with the business instead of
  refiling a closed quarter.
- Cut daily ingestion of a MongoDB collection of 15 million documents from about 3 hours to 15
  minutes with bounded read windows, materialized Delta staging and an explicit destination schema
  in place of inference.
- Built job-level cost attribution from the Databricks billing system tables and used it to
  reverse a move to serverless compute that showed a 1.5x per-DBU gap. Right-sized the classic
  Photon clusters from observed core-hours and disk spill, and documented the runtime regression
  accepted in the trade.

### Tech

<table>
  <tr>
    <td><b>Languages &amp; processing</b></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
      <img src="https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" alt="SQL" />
      <img src="https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" alt="PySpark" />
      <img src="https://img.shields.io/badge/Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white" alt="Polars" />
      <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
      <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
      <img src="https://img.shields.io/badge/PyArrow-E25A1C?style=for-the-badge&logo=apache&logoColor=white" alt="PyArrow" />
    </td>
  </tr>
  <tr>
    <td><b>Data engineering &amp; orchestration</b></td>
    <td>
      <img src="https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white" alt="dbt" />
      <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white" alt="Airflow" />
      <img src="https://img.shields.io/badge/Astronomer_Cosmos-4E2A8E?style=for-the-badge&logo=astronomer&logoColor=white" alt="Cosmos" />
      <img src="https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Kafka" />
      <img src="https://img.shields.io/badge/Debezium-91D443?style=for-the-badge&logoColor=white" alt="Debezium" />
      <img src="https://img.shields.io/badge/Delta_Lake-003366?style=for-the-badge&logo=delta&logoColor=white" alt="Delta Lake" />
      <img src="https://img.shields.io/badge/Apache_Iceberg-2A6DB2?style=for-the-badge&logoColor=white" alt="Apache Iceberg" />
      <img src="https://img.shields.io/badge/Protobuf-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Protobuf" />
      <img src="https://img.shields.io/badge/Avro-1A5B8C?style=for-the-badge&logo=apache&logoColor=white" alt="Avro" />
      <img src="https://img.shields.io/badge/NiFi-728E9B?style=for-the-badge" alt="NiFi" />
      <img src="https://img.shields.io/badge/DVC-13ADC7?style=for-the-badge&logo=dvc&logoColor=white" alt="DVC" />
      <img src="https://img.shields.io/badge/Elementary-6B4FBB?style=for-the-badge" alt="Elementary" />
    </td>
  </tr>
  <tr>
    <td><b>Platforms &amp; cloud</b></td>
    <td>
      <img src="https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white" alt="Databricks" />
      <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="Azure" />
      <img src="https://img.shields.io/badge/Unity_Catalog-FF3621?style=for-the-badge&logo=databricks&logoColor=white" alt="Unity Catalog" />
      <img src="https://img.shields.io/badge/Confluent-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Confluent" />
    </td>
  </tr>
  <tr>
    <td><b>Data stores &amp; query engines</b></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
      <img src="https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL Server" />
      <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB" />
      <img src="https://img.shields.io/badge/Trino-DD00A1?style=for-the-badge&logo=trino&logoColor=white" alt="Trino" />
      <img src="https://img.shields.io/badge/ADLS_Gen2-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white" alt="ADLS Gen2" />
    </td>
  </tr>
  <tr>
    <td><b>DevOps &amp; tooling</b></td>
    <td>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
      <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />
      <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white" alt="uv" />
      <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux" />
      <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Bash" />
    </td>
  </tr>
  <tr>
    <td><b>Frameworks &amp; libraries</b></td>
    <td>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
      <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
      <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic" />
      <img src="https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white" alt="Jinja2" />
      <img src="https://img.shields.io/badge/Scrapy-60A839?style=for-the-badge&logo=scrapy&logoColor=white" alt="Scrapy" />
      <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest" />
      <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />
      <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
      <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white" alt="Spring Boot" />
      <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt="React" />
    </td>
  </tr>
</table>

<a href="https://github.com/emanuel-luis/data-engineering-projects" title="Open the data engineering portfolio index">
  <img src="./images/de-banner.png" width="100%" alt="Data Engineer Portfolio: open the project index" />
</a>

### Projects

Personal projects, built on open or synthetic data.

#### Ingestion

| Project | What it does |
| --- | --- |
| [books-scraping](https://github.com/emanuel-luis/books-scraping) | Re-runnable crawl of the Books to Scrape sandbox (1,000 books) into a raw landing zone of HTML plus a manifest, then validated Parquet and a DuckDB serving layer. Loads upsert by UPC, so loading the same run twice changes nothing. |
| [ecommerce-scraping](https://github.com/emanuel-luis/ecommerce-scraping) | Scrapy crawler for three Brazilian fashion stores. It reads the schema.org Product JSON-LD in server-rendered pages, so it needs no browser, and writes redacted raw pages, Parquet partitioned by store and run date, and DuckDB views. |
| [ingestion-toolkit](https://github.com/emanuel-luis/ingestion-toolkit) | CLI that writes validated ingestion configs (full scan, incremental watermark, CDC) and renders each one into an Airflow 3 DAG with landing, bronze, rejects and run metadata. The watermark advances in the load transaction, so a retried run is idempotent. |
| [mssql-cdc-pyspark](https://github.com/emanuel-luis/mssql-cdc-pyspark) | PySpark streaming source for SQL Server CDC on Spark's Python DataSource V2 API. Offsets are commit LSNs, and a `finalized_until` signal tells downstream jobs when a period of data is safe to read. On [PyPI](https://pypi.org/project/mssql-cdc-pyspark/), with a [docs site](https://emanuel-luis.github.io/mssql-cdc-pyspark/). |

#### Streaming and CDC

| Project | What it does |
| --- | --- |
| [cdc-streaming-demo](https://github.com/emanuel-luis/cdc-streaming-demo) | Postgres changes go through Debezium and Kafka (Protobuf, Schema Registry) into an append-only Delta log written by Spark Structured Streaming, then into dbt-duckdb marts and a Streamlit dashboard. `make demo` checks 200 seeded mutations end to end, and one laptop run measured a p50 commit-to-lake lag of 41.7 s. A second path reads SQL Server CDC through mssql-cdc-pyspark. |
| [kafka-streaming-lakehouse](https://github.com/emanuel-luis/kafka-streaming-lakehouse) | Avro events flow through Kafka and Schema Registry into Apache Iceberg. A two-replica consumer group appends bronze idempotently and sends undecodable records to a DLQ; Spark Structured Streaming builds silver, Spark batch jobs build gold, and Trino queries every layer. `lakestream check` reconciles each layer with the run manifest. |

#### Lakehouse and modeling

| Project | What it does |
| --- | --- |
| [de-lakehouse-pipeline](https://github.com/emanuel-luis/de-lakehouse-pipeline) | ELT on Olist-shaped e-commerce data (seeded synthetic by default, or the open Olist dataset from Kaggle): Polars ingestion with typed data contracts, then dbt staging, bronze, intermediate and marts on DuckDB. An hourly Airflow 3 DAG runs each dbt model and test as its own task through Astronomer Cosmos, and Elementary reports on data quality. The dbt docs and the Elementary report are [on GitHub Pages](https://emanuel-luis.github.io/de-lakehouse-pipeline/). |
| [vaccine-warehouse](https://github.com/emanuel-luis/vaccine-warehouse) | Kimball-style warehouse for Brazilian childhood vaccination on Postgres, with Python ELT and dbt marts as the batch layer. A Spring Boot API adds a live speed layer with idempotent ingest and a watermark that keeps a dose from being counted twice, and a React dashboard behind Keycloak reads from it. Reference data is public; doses are synthetic. |

#### ML pipelines

| Project | What it does |
| --- | --- |
| [covid19-xray-pipeline](https://github.com/emanuel-luis/covid19-xray-pipeline) | DVC pipeline over three public chest X-ray datasets: 41,077 images after deduplication, group-aware splits with no leakage between them, 119 handcrafted features and a ResNet-18. On the same test split, the MLP baseline scores F1 0.9446 and the ResNet-18 0.9830. |
| [necrohub](https://github.com/emanuel-luis/necrohub) | Pipeline over synthetic pt-BR necropsy reports: generate, de-identify, fine-tune encoders and retrieve through pgvector. CI fails unless a clean run reproduces the committed `dvc.lock` and metrics. On held-out templates, a fine-tuned BioBERTpt encoder reaches strict PII F1 0.9444, against 0.6667 for regex. Synthetic data only. |

#### Applications

| Project | What it does |
| --- | --- |
| [bank-credit](https://github.com/emanuel-luis/bank-credit) | Credit-request workflow (FastAPI, Postgres, React). One service writes every state change to an append-only event log, enforced by a Postgres trigger and an ORM guard. SLA analytics are versioned SQL views, and exports are published with a manifest and sha256 only when their contract checks pass. |

### Open-source contributions

Two merged pull requests to [Astronomer Cosmos](https://github.com/astronomer/astronomer-cosmos), the
library that integrates dbt with Airflow:

- [#2201](https://github.com/astronomer/astronomer-cosmos/pull/2201) (December 2025):
  `DbtConsumerWatcherSensor` now carries the `template_fields` of `DbtRunLocalOperator`, so
  Watcher-mode sensors render Airflow templates when they fall back to local execution
  ([#2193](https://github.com/astronomer/astronomer-cosmos/issues/2193)). Includes tests.
- [#2241](https://github.com/astronomer/astronomer-cosmos/pull/2241) (January 2026): restores
  plain-text dbt logs, with CLI colors, in `ExecutionMode.WATCHER`. `FullOutputSubprocessHook` now
  logs through a `process_log_line` callable, and JSON output applies only to the `SUBPROCESS`
  invocation mode.

### Publications

Two 2022 publications from the COVID-19 research behind
[covid19-xray-pipeline](https://github.com/emanuel-luis/covid19-xray-pipeline), whose MLP baseline
re-implements the method of the first paper:

- Sousa Filho, E. L. C. de; Magno, P. G. S.; Santos, C. J. P.; Silva, G. L. F. da; Diniz, J. O. B.;
  Quintanilha, D. B. P. "Um Método Baseado em Radiomics e MLP para Diagnóstico Automático de
  COVID-19 a partir de Raio-X de Tórax" (a radiomics and MLP method for automatic COVID-19 diagnosis
  from chest X-rays). Anais da X ERCEMAPI, SBC, 2022, pp. 188-197.
  [doi:10.5753/ercemapi.2022.226508](https://doi.org/10.5753/ercemapi.2022.226508)
- Silva, G.; S. Filho, E.; Magno, P.; Santos, C.; Diniz, J.; Ferreira, J.; Matos, C.; Silva, A.
  "Desenvolvimento de uma aplicação web para o diagnóstico da COVID-19 usando conceitos, técnicas e
  ferramentas de Inteligência Artificial" (book chapter on building a web application for COVID-19
  diagnosis with AI). Minicursos da ERCEMAPI 2022, SBC, 2022, pp. 122-139.
  [doi:10.5753/sbc.11014.1.6](https://doi.org/10.5753/sbc.11014.1.6)

### Certifications

- [Databricks Certified Data Engineer Associate](https://credentials.databricks.com/ae7ff0a4-3dc9-40cf-bec0-641bd7b17c25) · Databricks · Sep 2026 (valid until Sep 2028)
- [Academy Accreditation: Azure Databricks Platform Architect](https://credentials.databricks.com/093bdac8-564d-42ff-bef3-69e79efe5455) · Databricks · Aug 2026
- [Academy Accreditation: Generative AI Fundamentals](https://credentials.databricks.com/bda55fe5-8262-45c8-9a8a-9ff9e389ed81) · Databricks · Aug 2026
- [Academy Accreditation: Databricks Fundamentals](https://credentials.databricks.com/15313a3a-ae9a-4bfa-847e-ce6a9246786c) · Databricks · May 2026
- [SQL (Advanced)](https://www.hackerrank.com/certificates/f3f8890609be) · HackerRank

<details>
<summary>Courses</summary>

- [Python 3: Curso Completo do Básico ao Avançado](https://www.udemy.com/certificate/UC-a1ac8f23-95bd-4b27-8133-d474faef3c44/) · Udemy (Cod3r) · Jul 2021 · 26 h
- [C# Advanced Topics: Prepare for Technical Interviews](https://www.udemy.com/certificate/UC-1abc88b4-95e7-4e97-aaff-2471a71566da/) · Udemy (Mosh Hamedani) · Oct 2020 · 3 h
- [C# Intermediate: Classes, Interfaces and OOP](https://www.udemy.com/certificate/UC-ec641ed1-8d1d-436f-a2b9-3388e9a8958d/) · Udemy (Mosh Hamedani) · Jul 2020 · 6 h
- [C# Basics for Beginners: Learn C# Fundamentals by Coding](https://www.udemy.com/certificate/UC-319fe684-5ec0-48e0-8c7f-4248932ed54d/) · Udemy (Mosh Hamedani) · May 2020 · 5.5 h
- [C# Curso Completo: Do Básico ao Avançado!](https://www.udemy.com/certificate/UC-1fb01566-9f25-4c3a-ae4f-da1ff8465ed6/) · Udemy (Cod3r) · May 2020 · 16.5 h
- [Git e GitHub para iniciantes](https://www.udemy.com/course/git-e-github-para-iniciantes/) · Udemy · completed, no certificate

</details>

### GitHub analytics

<div align="center">
  <img width="53%" alt="GitHub stats" src="assets/stats.svg"/>
  <img width="37%" alt="Most used languages" src="assets/top-langs.svg"/>
</div>

<div align="center">
  <img width="90%" src="https://streak-stats.demolab.com?user=emanuel-luis&theme=tokyonight&hide_border=true"/>
</div>

<details>
<summary>Education &amp; training</summary>

- B.S. Software Engineering, UNDB (Unidade de Ensino Superior Dom Bosco), São Luís, Brazil · 2021 to 2025
- Computer Vision Training · Data Inception · May 2022
- Machine Learning Training · Data Inception · Mar 2022

</details>
