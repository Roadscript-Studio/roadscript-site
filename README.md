# Roadscript Site

`roadscript-site` is the public website and demo surface for Roadscript.

Roadscript is an authenticity tooling project focused on media provenance, invisible watermarking workflows, and verification-oriented product experiences. This repository presents the public-facing website, sample-driven demo flow, and local mock backend contract used to communicate the product direction without exposing the private core engine implementation.

## Repository role

This repository is part of the Roadscript public/private repository ecosystem:

| Repository | Visibility | Purpose |
|---|---:|---|
| [`roadscript-docs`](https://github.com/Roadscript-Studio/roadscript-docs) | Public | Public overview, architecture notes, repository boundaries, and development milestones. |
| [`roadscript-cli`](https://github.com/Roadscript-Studio/roadscript-cli) | Public | Standalone CLI, workflow DSL, local TUI prototype, examples, tests, and tooling. |
| [`roadscript-site`](https://github.com/Roadscript-Studio/roadscript-site) | Public | Public website and sample-driven demo surface. |
| `roadscript-engine` | Private | Private C++ core package consumed by the application layer. |

The site is intentionally separated from the private engine. It demonstrates product flow and system behavior at the presentation layer while engine integration remains under active development.

## Current status

- Static multi-page website
- Public product overview and roadmap pages
- Sample-driven verification workflow demo
- Frontend mock demo data for deployed static hosting
- Minimal FastAPI mock backend contract for local development and future integration
- No production engine execution in this repository

The current demo is intentionally sample-driven. It is designed to communicate Roadscript’s product direction and verification workflow without claiming production readiness.

## Tech stack

- Static HTML, CSS, and vanilla JavaScript
- FastAPI for the local mock backend contract
- Cloudflare Pages hosting for the public website

There is no frontend build step in this repository. The public website is a lightweight static site.

## Website pages

- `index.html` — homepage and product overview
- `demo.html` — interactive verification workflow demo
- `roadmap.html` — product and engineering roadmap
- `whitepaper.html` — product thesis and technical direction summary

## Local development

### Preview the static website

From the `Website` repository root:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://127.0.0.1:8080/index.html
http://127.0.0.1:8080/demo.html
```

By default, the deployed site and local static preview use frontend mock demo data from:

```text
scripts/demoMockData.js
```

That means `demo.html` works without the FastAPI backend.

### Run the mock backend contract

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

Start the mock backend:

```bash
uvicorn backend.main:app --reload
```

The local API will be available at:

```text
http://127.0.0.1:8000/api/health
http://127.0.0.1:8000/api/demo/embed
```

The frontend demo currently uses frontend mock data by default. The FastAPI backend remains available as a local development contract for future integration work. See [`backend/README.md`](backend/README.md) for the response shape and local CORS notes.

### Useful commands

```bash
# Preview the static site
python3 -m http.server 8080

# Run the mock backend
uvicorn backend.main:app --reload

# Validate backend modules
python3 -m compileall backend
```

## Repository structure

```text
.
├── assets/
│   ├── brand/
│   │   ├── favicon.svg
│   │   └── wordmark.svg
│   └── demo/
│       └── README.md
├── scripts/
│   └── demoMockData.js
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

## Demo behavior

The public-facing demo is currently driven by preset sample selections.

- Deployed pages read sample results from `scripts/demoMockData.js`.
- The FastAPI backend returns mock verification results using a typed response contract.
- Missing demo image assets are handled by the UI fallback state.
- Workflow states in `demo.html` are simulated to preview the future verification experience.
- No real engine execution, upload processing, or production verification job is performed by this repository.

Backend mode can be re-enabled later by changing `USE_FRONTEND_MOCK_DATA` in `demo.html` and pointing `window.DEMO_API_BASE` to the desired API host.

## Roadmap

Planned directions include:

- Real custom upload workflow
- Backend integration with the private Roadscript engine package
- Account and credit system for productized runs
- Packaged CLI and desktop/app releases
- More complete public demo assets and product documentation

These items are under active development and should not be interpreted as production availability.

## Related repositories

- [`roadscript-docs`](https://github.com/Roadscript-Studio/roadscript-docs) — public overview, architecture notes, and repository boundaries.
- [`roadscript-cli`](https://github.com/Roadscript-Studio/roadscript-cli) — standalone CLI, workflow DSL, local TUI prototype, examples, tests, and tooling.
- `roadscript-engine` — private C++ core package used behind the application layer.

## Repo hygiene

- Editor files, Python cache files, virtual environments, and system junk should remain untracked.
- Website build artifacts such as `node_modules/`, `dist/`, `build/`, and `.vite/` should remain untracked.
- No secrets, tokens, production credentials, or private keys belong in this repository.
- Sample/demo behavior should remain clearly separated from real engine execution code.

## License / status

Roadscript is an active independent product-engineering project.

All rights reserved © 2026 Roadscript.
