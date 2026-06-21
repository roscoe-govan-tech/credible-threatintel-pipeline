# Credible Threat Intelligence Pipeline

A Python-based threat intelligence pipeline that collects cybersecurity advisories from configured sources, generates concise summaries, stores structured records in SQLite, applies basic prioritization logic, and presents the results through a Streamlit dashboard.

## Project Purpose

This project was created as a hands-on learning and portfolio exercise focused on cybersecurity operations, Python development, data engineering concepts, and analyst-oriented automation.

The goal is to better understand how threat intelligence data moves through a practical workflow:

1. Source collection
2. Parsing and normalization
3. Enrichment and summarization
4. Duplicate detection
5. Database storage
6. Prioritization
7. Analyst presentation

The project is currently a functional prototype and remains under active development.

## Current Capabilities

The current version includes:

* Collection of RSS-based cybersecurity advisories
* Source configuration through YAML
* Standardized parsing of:

  * Source name
  * Source tier
  * Category
  * Title
  * URL
  * Summary
  * Publication date
* SHA-256 content hashing for duplicate prevention
* SQLite storage for collected intelligence records
* Rule-based TL;DR summary generation without requiring an external API
* Basic priority scoring based on source, category, and title context
* Streamlit dashboard with:

  * Total item, source, and category metrics
  * Source and category filters
  * Minimum threat-score filtering
  * Top-threat display
  * Raw intelligence table
  * Analyst-friendly intelligence cards
  * Links to original reports

## Technologies Used

* Python
* SQLite
* Streamlit
* pandas
* feedparser
* PyYAML
* YAML configuration
* RSS processing
* SHA-256 hashing
* Git and GitHub

## Project Structure

```text
credible-threatintel-pipeline/
├── config/
│   └── sources.yml
├── data/
│   └── threatintel.db
├── src/
│   ├── collectors/
│   │   └── rss_collector.py
│   ├── dashboard/
│   │   └── app.py
│   ├── db/
│   │   ├── database.py
│   │   └── schema.sql
│   ├── digest/
│   │   └── generate_digest.py
│   ├── parsers/
│   │   ├── extract_cves.py
│   │   ├── extract_keywords.py
│   │   └── summarizer.py
│   ├── scoring/
│   │   └── score_intel.py
│   └── main.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How the Pipeline Works

### 1. Source Configuration

Threat intelligence sources are defined in:

```text
config/sources.yml
```

Each source includes:

* Name
* URL
* Source tier
* Intelligence category

### 2. Collection

The RSS collector retrieves entries from compatible RSS feeds and extracts the available title, URL, summary, and publication date.

```text
src/collectors/rss_collector.py
```

### 3. Duplicate Prevention

Each record receives a SHA-256 hash generated from its title and URL.

The `content_hash` field is stored as unique in SQLite, allowing duplicate records to be skipped automatically.

### 4. Summary Generation

The project currently uses a lightweight rule-based summarizer that creates a concise TL;DR from the title and available RSS content.

```text
src/parsers/summarizer.py
```

This approach does not require an external AI service or API key.

### 5. Database Storage

Collected records are stored in:

```text
data/threatintel.db
```

The current schema includes:

* Source name
* Source tier
* Category
* Title
* URL
* Original summary
* Generated TL;DR
* Publication date
* Content hash
* Collection timestamp

### 6. Priority Scoring

The dashboard currently applies basic rule-based scoring. Examples include:

* Higher weighting for CISA sources
* Additional weighting for exploitation-related categories
* Additional weighting when ransomware appears in a title
* Additional weighting for Microsoft advisories

This scoring model is intentionally simple and will be expanded in future versions.

### 7. Dashboard

The Streamlit dashboard reads records from SQLite and provides an analyst-oriented view of the collected intelligence.

Current dashboard features include:

* KPI metrics
* Source filters
* Category filters
* Threat-score filtering
* Top-threat ranking
* Raw intelligence table
* Individual intelligence cards
* Direct links to source material

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/roscoe-govan-tech/credible-threatintel-pipeline.git
```

### 2. Enter the Project Directory

```bash
cd credible-threatintel-pipeline
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Pipeline

From the project root directory, run:

```bash
python src/main.py
```

The pipeline will:

1. Initialize the SQLite database
2. Load configured sources
3. Collect compatible RSS entries
4. Generate TL;DR summaries
5. Store new records
6. Skip duplicate records

## Running the Dashboard

After the pipeline has collected data, start the Streamlit dashboard with:

```bash
streamlit run src/dashboard/app.py
```

The dashboard will open in a local browser window.

## Current Limitations

This project is still under development. Current limitations include:

* The collector is designed for RSS-compatible sources.
* JSON-based sources such as CISA KEV and NVD require dedicated collectors and are not yet fully supported by the current RSS collector.
* Dedicated CVE extraction is not yet implemented.
* Dedicated keyword extraction is not yet implemented.
* Digest generation is not yet implemented.
* Priority scoring currently exists in the dashboard and has not yet been separated into the dedicated scoring module.
* Automated scheduling, formal testing, and production-grade logging are not yet implemented.
* The current summarizer is rule-based rather than model-driven.

## Planned Improvements

Planned enhancements include:

* Add dedicated JSON collectors for CISA KEV and NVD
* Implement CVE extraction
* Implement keyword and indicator extraction
* Move scoring into a reusable scoring module
* Expand scoring with:

  * Known exploitation status
  * CVSS severity
  * EPSS probability
  * Vendor and product relevance
  * Threat-actor or ransomware context
* Add digest generation
* Add scheduled pipeline execution
* Improve error handling and logging
* Add automated tests
* Add source-health monitoring
* Add industry-specific filtering
* Add richer dashboard visualizations
* Add optional API-based enrichment and summarization

## Example Analyst Use Case

A security analyst may need to review advisories from multiple trusted sources and determine which items deserve immediate attention.

This pipeline helps by:

* Collecting intelligence in one place
* Removing duplicate records
* Creating concise summaries
* Applying basic prioritization
* Allowing analysts to filter by source, category, and score
* Linking directly to original reports for deeper investigation

## Development Approach

This project uses AI-assisted development as part of the learning process. AI has been used to help generate and structure portions of the code, while the project owner reviews the logic, tests components, troubleshoots issues, and builds practical understanding of the underlying Python, database, security, and data-engineering concepts.

## Security and Data Handling

This project uses publicly available threat intelligence sources and does not contain confidential employer data, customer information, production logs, or proprietary security records.

No external API keys are required for the current rule-based version.

## Project Status

**Functional prototype — active development**

The RSS collection, duplicate prevention, SQLite storage, TL;DR generation, basic dashboard scoring, filtering, and Streamlit presentation are currently implemented.

Additional collectors, extraction modules, enrichment logic, testing, and automation are planned.

## Disclaimer

This project is intended for learning, portfolio development, and demonstration of cybersecurity and data-engineering concepts.

It is not intended to replace commercial threat intelligence platforms, vulnerability-management systems, SIEM products, or professional threat-intelligence services.
