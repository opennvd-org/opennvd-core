# OpenNVD Core

Community-powered CVE/CWE vulnerability data mirror and tooling, maintained by [OpenNVD](https://opennvd.io).


## Overview

This repository hosts the core tools and directory structure for downloading and managing CVE (Common Vulnerabilities and Exposures) and CWE (Common Weakness Enumeration) data. It is part of the [OpenNVD Project](https://opennvd.io), an open alternative to the National Vulnerability Database (NVD).

This repository includes:

- JSON mirror of CVE and CWE datasets (NVD, MITRE)
- Scripts for syncing, filtering, and formatting data
- Docs for deployment, architecture and API usage (coming soon)

## How to Use

1. Clone the Repository
```bash
git clone git@github.com:opennvd-org/opennvd-core.git
cd opennvd-core
```

2. Create a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
```bash
pip install requests tqdm
```

4. Run the Download Script
```bash
python scripts/download_cve_json.py
```

This will download and save the latest CVE data to the data/cve/ folder:
data/cve/
├── nvdcve-1.1-2023.json.gz
├── nvdcve-1.1-2024.json.gz
├── nvdcve-1.1-recent.json.gz
└── nvdcve-1.1-modified.json.gz

You can extract and inspect them with gunzip and jq, e.g.:
```bash
gunzip -c data/cve/nvdcve-1.1-2023.json.gz | jq '.CVE_Items | length'
```  

## Live Project Website

> [https://opennvd.io](https://opennvd.io) — *The Open National Vulnerability Database*

## Project Structure
opennvd-core/
├── data/              # CVE and CWE data folders
│   └── cve/           # CVE JSON files (.gitkeep committed, actual data ignored)
├── docs/              # Documentation and project specs
├── scripts/           # Python tools and sync scripts
│   └── download_cve_json.py
├── venv/              # Local virtual environment (not committed)
├── LICENSE
└── README.md


## Roadmap

1. CVE JSON downloader ---- working on it
2. JSON-to-structured transformation
3. CWE parsing and linking
4. REST API or CLI tools
5. GitHub Actions for auto sync

## License

This project is licensed under the MIT License.
