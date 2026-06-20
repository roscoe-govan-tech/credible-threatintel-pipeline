# Credible Threat Intel Pipeline

A Python-based threat intelligence pipeline for ingesting, parsing, scoring, and summarizing vulnerability and threat data from trusted security sources to support analyst workflows and defensive prioritization.

## Project Purpose

This project was built to practice Python, data parsing, automation, and security-focused data engineering concepts. The goal is to collect threat intelligence data, extract useful vulnerability details, organize the data, and produce analyst-friendly summaries that can support prioritization and defensive decision-making.

## What This Project Does

* Collects threat and vulnerability intelligence from configured sources
* Parses vulnerability data such as CVE IDs, vendors, products, descriptions, and references
* Extracts useful keywords and security-relevant details
* Stores structured threat intelligence data
* Scores or prioritizes findings based on available context
* Generates summaries for analyst review

## Skills Demonstrated

* Python scripting
* Threat intelligence processing
* Data parsing and transformation
* JSON handling
* File and directory organization
* SQLite/database concepts
* Security analysis fundamentals
* Automation workflow design
* Git and GitHub project documentation

## Project Structure

```text
credible-threatintel-pipeline/
├── config/              # Configuration files
├── data/                # Local data storage
├── src/                 # Source code
├── .env.example         # Example environment variable file
├── .gitignore           # Files excluded from Git tracking
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

## Example Use Case

A security analyst may need to review newly published vulnerabilities and determine which ones deserve attention. This pipeline helps organize raw vulnerability data into a more structured format so it can be reviewed, filtered, and prioritized more efficiently.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/roscoe-govan/credible-threatintel-pipeline.git
```

2. Navigate into the project folder:

```bash
cd credible-threatintel-pipeline
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a local `.env` file using `.env.example` as a guide.

6. Run the main script:

```bash
python src/main.py
```

## Current Status

This project is under active development. Current focus areas include improving source collection, parsing logic, scoring, database storage, and summary generation.

## Future Improvements

* Add more threat intelligence sources
* Improve CVE and keyword extraction
* Add stronger scoring logic
* Add dashboard or reporting output
* Add automated scheduled runs
* Improve error handling and logging
* Add tests for parsing and scoring functions

## Notes

This project is intended for learning, portfolio development, and practical security/data engineering skill-building. It is not intended to replace commercial threat intelligence platforms.
