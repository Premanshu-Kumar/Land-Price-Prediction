# Installation — macOS ARM64 (Apple Silicon)

## Prerequisites

- **Python 3.11** installed (verify: `python3.11 --version`)
- **Xcode Command Line Tools** (for lxml compilation): `xcode-select --install`

## Setup

### 1. Create and Activate Virtual Environment

```bash
cd "/Users/soumyadebtripathy/Project Aurelius"
python3.11 -m venv .venv
source .venv/bin/activate
```

### 2. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Install Playwright Browser Binaries

Playwright ships pre-built ARM64 binaries for macOS. Run:

```bash
playwright install
```

This downloads Chromium, Firefox, and WebKit browsers into:
`~/Library/Caches/ms-playwright/`

To install **only Chromium** (smaller download, sufficient for this project):

```bash
playwright install chromium
```

### 4. Verify Installation

```bash
python3.11 -c "from playwright.sync_api import sync_playwright; print('Playwright OK')"
python3.11 -c "import pandas; print(f'Pandas {pandas.__version__} OK')"
python3.11 -c "from bs4 import BeautifulSoup; print('BeautifulSoup OK')"
python3.11 -c "from fake_useragent import UserAgent; print(f'UA: {UserAgent().random[:50]}...')"
python3.11 -c "import sqlite3; print(f'SQLite {sqlite3.sqlite_version} OK')"
```

All five checks should print "OK".

## Running the Scraper

```bash
source .venv/bin/activate
python3.11 src/scraper/collector.py
```

Output:

- Database: `data/raw/punjab_real_estate.db`
- Logs: `data/raw/scraper.log`

## Troubleshooting

| Issue                             | Solution                                            |
| --------------------------------- | --------------------------------------------------- |
| `lxml` build fails                | Run `xcode-select --install` and retry              |
| Playwright browser download hangs | Set `PLAYWRIGHT_BROWSERS_PATH=0` to use local cache |
| `fake-useragent` import error     | Ensure version `>=2.0.0` (pure Python, no C deps)   |
| Permission denied on `.venv`      | Run `chmod -R u+rwx .venv`                          |
