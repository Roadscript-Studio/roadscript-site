# Roadscript Website

Roadscript is a product and engineering project focused on invisible watermarking for image authenticity, provenance, and verification workflows.

This repository contains the recruiter-facing Roadscript website, a sample-driven product demo, and a minimal
FastAPI mock backend contract used to simulate verification results during local development.

## Current status

- Static multi-page website
- Product-oriented demo experience for the watermark verification workflow
- FastAPI mock backend for sample-based demo responses
- No production engine execution in this repo yet

The current demo is intentionally sample-driven. It is designed to communicate product direction and system behavior cleanly while backend engine integration is still in progress.

## Tech stack

- Static HTML, CSS, and vanilla JavaScript
- FastAPI for the mock demo backend contract
- Cloudflare Pages hosting for the public website

There is no frontend build step in this repository. The public website is a lightweight static site.

## Website pages

- `index.html`
  Homepage and product overview
- `demo.html`
  Interactive verification workflow demo
- `roadmap.html`
  Product and engineering roadmap
- `whitepaper.html`
  Product thesis and technical direction summary

## Local development

### 1. Preview the static website

From the repository root:

```bash
python3 -m http.server 8080
```

Then open:

- `http://127.0.0.1:8080/index.html`
- `http://127.0.0.1:8080/demo.html`

### Available commands

- Preview the static site:
  `python3 -m http.server 8080`
- Run the mock backend:
  `uvicorn backend.main:app --reload`
- Validate backend modules:
  `python3 -m compileall backend`

### 2. Run the mock backend contract

Create and activate a virtual environment, then install backend requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

The demo backend will be available at:

- `http://127.0.0.1:8000/api/health`
- `http://127.0.0.1:8000/api/demo/embed`

The frontend demo calls `http://127.0.0.1:8000` by default. See `backend/README.md` for the backend contract
details and local CORS notes.

## Repository structure

```text
.
├── assets/
│   ├── brand/
│   │   ├── favicon.svg
│   │   └── wordmark.svg
│   └── demo/
│       └── README.md
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── README.md
│   ├── requirements.txt
│   └── services/
│       ├── demo_service.py
│       └── mock_samples.py
├── demo.html
├── index.html
├── roadmap.html
├── whitepaper.html
├── robots.txt
├── sitemap.xml
└── README.md
```

## Mock demo notes

- The public-facing demo is currently driven by preset sample selections.
- The FastAPI backend returns mock verification results using a typed response contract.
- Missing demo image assets are handled gracefully by the UI fallback state.
- The workflow states in `demo.html` are intentionally simulated to preview the future verification experience without claiming production readiness.

## Roadmap

- Real custom upload workflow
- Backend engine integration for watermark embed and verify operations
- Credit and account system for productized runs
- Packaged CLI and desktop/app releases

## Repo hygiene

- Editor files, Python cache files, virtual environments, and system junk should remain untracked
- No secrets or production credentials belong in this repository
- Sample/demo behavior should remain clearly separated from real engine execution code

## License / status

Roadscript is an active independent product-engineering project.

All rights reserved © 2026 Roadscript.
