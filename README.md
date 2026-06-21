# Credible Threat Intelligence Pipeline

A Python-based threat intelligence pipeline that collects security advisories from trusted public sources, normalizes the data, prevents duplicate records, stores results in SQLite, generates concise analyst summaries, applies basic prioritization logic, and presents the intelligence through a Streamlit dashboard.

## Project Overview

This project was created as a hands-on cybersecurity and data-engineering exercise focused on understanding how threat intelligence moves through a practical workflow.

The current pipeline demonstrates:

1. Source configuration
2. RSS collection
3. Data normalization
4. Summary generation
5. Duplicate prevention
6. SQLite storage
7. Basic threat prioritization
8. Dashboard presentation

The project is a functional prototype and remains under active development.

## Why I Built It

Security analysts often review information from multiple vendors, government agencies, and threat-research organizations. That information can arrive in different formats and may contain duplicate or low-priority content.

The goal of this project is to explore how Python and lightweight data-engineering techniques can help organize that information into a more consistent and analyst-friendly format.

The project also supports my continued development in:

* Python
* Data pipelines
* Security automation
* Threat intelligence
* Log and data processing
* SQLite
* Structured data analysis
* Analyst reporting
* Engineering-oriented security workflows

## Current Capabilities

The current version includes:

* YAML-based threat-source configuration
* Collection from compatible RSS feeds
* Standardized extraction of:

  * Source name
  * Source tier
  * Category
  * Title
  * URL
  * Source summary
  * Publication date
* SHA-256 content hashing
* Duplicate prevention through a unique database field
* SQLite storage
* Lightweight rule-based TL;DR generation
* Basic threat-priority scoring
* Streamlit dashboard
* Source and category filtering
* Minimum-score filtering
* Top-threat ranking
* Raw intelligence table
* Analyst-friendly intelligence cards
* Direct links to the original advisory or report

## Technology Stack

* Python
* Streamlit
* pandas
* SQLite
* feedparser
* PyYAML
* Beautiful Soup
* requests
* SHA-256 hashing
* Git and GitHub

## Project Structure

```text
credible-threatintel-pipeline/
├── config/
│   └── sources.yml
├── data/
│   └── threatintel.db
├── docs/
├── samples/
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
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── requirements-shortlist.txt
```

## How the Pipeline Works

### 1. Source Configuration

Threat-intelligence sources are defined in:

```text
config/sources.yml
```

Each source currently includes:

* Name
* URL
* Source tier
* Intelligence category

The source list contains both RSS and JSON-based sources. The current collector is designed for RSS-compatible feeds. Dedicated JSON collectors for sources such as CISA KEV and NVD are planned.

### 2. RSS Collection

The collector uses `feedparser` to retrieve entries from compatible feeds.

For each valid entry, it extracts:

* Title
* URL
* Summary
* Publication date
* Source metadata

Entries without a title or URL are skipped.

### 3. Duplicate Prevention

Each intelligence item receives a SHA-256 hash generated from its title and URL.

The SQLite schema stores `content_hash` as a unique value. When the same advisory appears again, the database uses `INSERT OR IGNORE` to prevent duplicate records.

### 4. Summary Generation

The current version uses a lightweight rule-based summarizer.

The summarizer:

* Combines the title and available RSS content
* Removes line breaks
* Limits excessively long feed content
* Produces a concise TL;DR for dashboard review

This version does not require an external AI API or API key.

### 5. SQLite Storage

Collected records are stored locally in:

```text
data/threatintel.db
```

The current schema stores:

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

### 6. Threat Prioritization

The Streamlit dashboard applies a basic rule-based priority score.

The current logic includes examples such as:

* Higher weighting for CISA sources
* Additional weighting for exploitation-related categories
* Additional weighting when ransomware appears in a title
* Additional weighting for Microsoft advisories

This is intentionally a simple prototype scoring model and is not intended to represent a production risk-scoring framework.

### 7. Streamlit Dashboard

The dashboard provides an analyst-oriented view of the collected intelligence.

Current dashboard features include:

* Total-item metric
* Source-count metric
* Category-count metric
* Source filtering
* Category filtering
* Minimum-score filtering
* Top-five threat display
* Raw intelligence table
* Detailed intelligence cards
* Color-coded priority indicators
* Links to original source reports

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

#### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

The repository contains two dependency files.

For the full frozen environment:

```bash
pip install -r requirements.txt
```

For the direct project dependencies:

```bash
pip install -r requirements-shortlist.txt
```

## Running the Collection Pipeline

From the project root, run:

```bash
python src/main.py
```

The pipeline will:

1. Initialize the SQLite database
2. Load configured sources
3. Collect compatible RSS entries
4. Generate TL;DR summaries
5. Insert new records
6. Skip duplicate records

## Running the Dashboard

After collecting data, launch the Streamlit dashboard:

```bash
streamlit run src/dashboard/app.py
```

Streamlit will normally open the dashboard at:

```text
http://localhost:8501
```

## Current Project Status

**Functional prototype under active development**

Currently implemented:

* RSS collection
* YAML source configuration
* Data normalization
* SHA-256 content hashing
* Duplicate prevention
* SQLite storage
* Rule-based TL;DR generation
* Dashboard-based scoring
* Streamlit filtering and presentation

The following files currently serve as placeholders for planned functionality:

* `src/parsers/extract_cves.py`
* `src/parsers/extract_keywords.py`
* `src/scoring/score_intel.py`
* `src/digest/generate_digest.py`

## Current Limitations

* The collector currently supports RSS-compatible feeds.
* JSON-based sources require dedicated collectors.
* CVE extraction is not yet implemented in the dedicated parser module.
* Keyword extraction is not yet implemented.
* Priority scoring currently exists inside the dashboard rather than the scoring module.
* Digest generation is not yet implemented.
* The summarizer is rule-based.
* Automated scheduling is not yet implemented.
* Formal unit and integration tests are not yet included.
* Production-grade logging and source-health monitoring are not yet implemented.

## Planned Improvements

Planned enhancements include:

* Add dedicated collectors for CISA KEV and NVD JSON feeds
* Implement CVE extraction
* Implement keyword and indicator extraction
* Move scoring into a reusable scoring module
* Add CVSS and EPSS enrichment
* Add known-exploitation weighting
* Add vendor and product relevance scoring
* Add threat-actor and ransomware context
* Add digest generation
* Add scheduled pipeline execution
* Improve logging and error handling
* Add automated tests
* Add source-health monitoring
* Add industry-specific views
* Add richer dashboard visualizations
* Improve summary quality and deduplication logic

## Example Analyst Use Case

A security analyst may need to review advisories from several trusted sources and determine which items deserve deeper investigation.

This pipeline helps by:

* Collecting compatible source content in one place
* Standardizing basic fields
* Removing duplicate records
* Creating concise summaries
* Applying simple prioritization
* Allowing filtering by source, category, and score
* Linking directly to original reports

## Development Approach

This project uses AI-assisted development as part of the learning and implementation process.

AI has been used to help generate and structure portions of the code. My role has included reviewing the logic, testing components, troubleshooting issues, validating output, refining the workflow, documenting the system, and building practical understanding of the Python, database, cybersecurity, and data-engineering concepts involved.

The project is intended to demonstrate both my existing analyst strengths and the engineering skills I am continuing to develop around security automation, structured data processing, and defensive workflows.

## Security and Data Handling

This project uses publicly available threat-intelligence sources.

It does not contain:

* Confidential employer data
* Customer information
* Production security logs
* Internal incident records
* Proprietary detection logic
* Credentials or API keys

Generated databases, logs, local environment files, and temporary data are excluded from Git tracking through `.gitignore`.

## Disclaimer

This project is intended for learning, portfolio development, and demonstration of cybersecurity and data-engineering concepts.

It is not intended to replace a commercial threat-intelligence platform, SIEM, vulnerability-management system, or professional threat-intelligence service.
