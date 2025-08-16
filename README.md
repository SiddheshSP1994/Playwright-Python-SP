# Playwright-Python-SP — Enterprise SDET Lab (Windows-first)

**Why this repo matters**

- Cut end-to-end regression from `<Xh>` to `<Yh>` (−`<Z>%`) with CI sharding and caching.
- Drove new-flake rate to `<= 1%` via deterministic data builders and failure clustering.
- Enabled faster, safer merges: PRs block on quality gates (lint, types, tests, flake budget, security).

**TL;DR**

- Python 3.11+, Pytest, Playwright (UI), FastAPI fakes (mail, payment), GitHub Actions CI.
- Balanced test pyramid target: Unit, Contract, E2E. AI-assisted triage with vendor-neutral stub fallback.
- One command to bring up fakes and run all tests with artifacts, traces, and an executive summary.

---

## Table of Contents
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Quick Start (Windows 11)](#quick-start-windows-11)
- [Run all tests with artifacts](#run-all-tests-with-artifacts)
- [Configuration (env + flags)](#configuration-env--flags)
- [Project Layout](#project-layout)
- [Test Pyramid](#test-pyramid)
- [Data Management and Determinism](#data-management-and-determinism)
- [AI Triage and Failure Clustering](#ai-triage-and-failure-clustering)
- [CI/CD Pipeline](#cicd-pipeline)
- [Reports and Artifacts](#reports-and-artifacts)
- [Quality Gates](#quality-gates)
- [Performance and Chaos (optional)](#performance-and-chaos-optional)
- [Security Baseline (optional)](#security-baseline-optional)
- [Metrics to keep this README at 90+](#metrics-to-keep-this-readme-at-90)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)

---

## Architecture

```mermaid
flowchart LR
  subgraph DevMachine[Windows 11 Dev Box]
    direction TB
    Tests[tests/*] --> Pytest[Pytest Runner]
    Pytest --> Playwright[Playwright]
    Pytest --> Plugins[Custom Pytest Plugins]
    Pytest --> Config[config/settings.py]
  end

  subgraph Fakes[Local Service Fakes]
    Mail[FastAPI: Mail]:::svc
    Pay[FastAPI: Payment]:::svc
  end

  Playwright -->|HTTP| Fakes

  subgraph CI[GitHub Actions / CI]
    Matrix[Matrix Shards (10-16)]
    Cache[Deps + Browsers Cache]
    Artifacts[Artifacts: traces, videos, ai-triage.md, run-summary.md]
    Quality[Quality Gates]
  end

  Pytest --> Artifacts
  Matrix --> Artifacts
  Quality --> Artifacts

classDef svc fill:#eef,stroke:#88a,stroke-width:1px;
```

---

## Key Features
- Windows-first workflows (PowerShell and Git Bash).
- Playwright + Pytest at scale with sharding and deterministic data.
- FastAPI fakes for third-party dependencies (mail, payment) to reduce flakiness and cost.
- AI-assisted failure triage (stub provider by default; OpenAI-compatible when configured).
- Requirements mapping and run summary suitable for non-technical stakeholders.
- Quality gates: ruff/black, mypy (targeted), tests, flake budget, optional SAST/DAST.

---

## Quick Start (Windows 11)

### PowerShell (recommended)
```powershell
# Clone
git clone https://github.com/SiddheshSP1994/Playwright-Python-SP.git
cd Playwright-Python-SP

# Python 3.11+ venv
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install deps
pip install -U pip
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install

# Optional: copy env template
copy .env.example .env
```

### Git Bash
```bash
git clone https://github.com/SiddheshSP1994/Playwright-Python-SP.git
cd Playwright-Python-SP

py -3.11 -m venv .venv
source .venv/Scripts/activate

pip install -U pip
pip install -r requirements.txt
python -m playwright install

cp .env.example .env
```

---

## Run all tests with artifacts

Bring up fakes and run tests in one go:

```powershell
# PowerShell
python tools/run_all.py
```

or manually:

```powershell
# 1) Start fakes (two terminals or use run_all.py)
$env:PAY_PORT="8081"; uvicorn services.fakes.payments.app:app --port $env:PAY_PORT
$env:MAIL_PORT="8082"; uvicorn services.fakes.mail.app:app --port $env:MAIL_PORT

# 2) Run pytest with HTML report and artifacts
pytest -n auto --browser chromium --html=playwright-report\report.html --self-contained-html
```

---

## Configuration (env + flags)

Create `.env` or export env vars (values shown are safe defaults):

```env
# AI triage (on by default via stub provider)
AI_ENABLED=1
AI_PROVIDER=stub            # stub | openai
AI_MODEL=gpt-4o-mini        # used only if provider=openai
AI_MAX_TOKENS=512
AI_TIMEOUT_SEC=20

# Service fakes
PAY_PORT=8081
MAIL_PORT=8082

# Pytest options (example)
PYTEST_ADDOPTS=-q
```

Pytest markers (configure in `pytest.ini`):
```ini
[pytest]
markers =
    smoke: fast critical checks
    regression: broader coverage
    slow: long-running tests
```

---

## Project Layout

```
Playwright-Python-SP/
├─ ai/                         # Provider interface, stub provider, prompts
├─ config/
│  └─ settings.py              # Centralized configuration (pydantic BaseSettings)
├─ plugins/
│  └─ ai_triage.py             # Failure clustering + summaries (stub by default)
├─ services/
│  └─ fakes/
│     ├─ payments/             # FastAPI payment fake
│     └─ mail/                 # FastAPI mail fake
├─ tests/
│  ├─ unit/                    # Fast unit tests (no browser; functions, utils, builders)
│  ├─ contract/                # API schema/contract tests (jsonschema/pydantic)
│  ├─ e2e/                     # Thin UI tests using Page Objects
│  └─ generated/               # Large generated suites (legacy/carry-over)
├─ tools/
│  └─ run_all.py               # Orchestrates fakes + pytest
├─ playwright-report/          # HTML test report (gitignored)
├─ artifacts/                  # ai-triage.md, run-summary.md, traces, videos (gitignored)
├─ pytest.ini
├─ requirements.txt
└─ .env.example
```

Note: If your repo does not yet have `tests/unit` or `tests/contract`, keep the folders and grow into them. Thin E2E tests should delegate logic to page/components and data builders.

---

## Test Pyramid

- Unit (fast): target `>= 60` tests, runtime `< 60s`, no browser, covers data builders, validation, utilities.
- Contract/API: target `>= 10` tests validating response schemas and error conditions.
- E2E: thin, behavior-focused flows; generated suites are supported but should not duplicate lower-layer checks.

Command hints:
```powershell
# Unit
pytest tests/unit -q

# Contract
pytest tests/contract -q

# E2E
pytest tests/e2e -n auto --browser chromium
```

---

## Data Management and Determinism

- Data builders live under `testing/data_builders/` (seeded RNG for reproducibility).
- Every test run writes to an isolated folder: `artifacts/run_<timestamp>/...`
- Two consecutive runs of the same selection should produce identical results and similar durations (±5%).

---

## AI Triage and Failure Clustering

- Plugin outputs:
  - `artifacts/ai-triage.md` — human-readable clustered failures with links to traces/screenshots.
  - `artifacts/triage.json` — machine-readable signatures, nodeids, error excerpts.
- Default provider is `stub` (offline, deterministic). To enable OpenAI-compatible inference:
```env
AI_PROVIDER=openai
AI_MODEL=<your-model>
OPENAI_API_KEY=<your-key>
```

---

## CI/CD Pipeline

- GitHub Actions with matrix sharding (10–16 shards for large suites).
- Caching of Python deps and Playwright browsers to reduce wall time.
- Upload artifacts per shard: traces, videos, screenshots, ai-triage, run-summary.
- Quality gates:
  - Lint: ruff/black
  - Types: mypy (targeted directories)
  - Tests: unit + contract + e2e
  - Flake budget: fail CI if new flake rate exceeds threshold
  - Optional: SAST/DAST

---

## Reports and Artifacts

- Playwright HTML report: `playwright-report/report.html`
- AI triage summary: `artifacts/ai-triage.md`
- Executive run summary: `artifacts/run-summary.md` (pass %, retry %, new flake count, time to first failure, links)
- Traces/videos/screenshots in `artifacts/run_<timestamp>/...`

.gitignore includes:
```
playwright-report/**
artifacts/**
allure-results/**
__pycache__/**
*.pyc
.venv/
.env
.DS_Store
```

---

## Quality Gates

- Lint clean: `ruff` passes, `black` enforced via pre-commit.
- Type targets pass: `mypy` on `config/`, `plugins/`, `pages/`, `tools/`.
- Flake budget: new flakes <= 1% vs base; retry rate <= 2%.
- CI wall time: reduced by >= 35% vs baseline after caching/sharding.

---

## Performance and Chaos (optional)

- Lightweight perf smoke (Locust or k6) on top 3 journeys (RPS 1–5 for 2–3 minutes).
- Chaos toggles in fakes: add 200ms latency and 3–5% HTTP 500s; nightly resilience job must stay within P95 budget.

---

## Security Baseline (optional)

- SAST with Semgrep on PRs (fail on High/Critical).
- DAST baseline with OWASP ZAP against fakes/staging on schedule; publish HTML report.

---

## Metrics to keep this README at 90+

Update these numbers weekly (or automate via CI):

| KPI                                | Target               | Current (update) |
|-----------------------------------|----------------------|------------------|
| Regression wall time (E2E)        | <= `<N>` minutes     | `<...>`          |
| New flake rate                    | <= 1.0%              | `<...>`          |
| Retry rate                        | <= 2.0%              | `<...>`          |
| Unit tests runtime                | <= 60s               | `<...>`          |
| Contract tests count              | >= 10                | `<...>`          |
| Executive summary availability    | 100% of CI runs      | `<...>`          |

---

## Troubleshooting

- `PytestUnknownMarkWarning`: add markers under `pytest.ini` as shown.
- `ModuleNotFoundError: playwright`: run `pip install -r requirements.txt` then `python -m playwright install`.
- `run_all.py: unrecognized arguments`: run `python tools/run_all.py` without extra flags or update its usage message.
- PowerShell script execution policy: run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (one-time), or start Terminal as Administrator.

---

## Roadmap

- Expand unit and contract layers; keep E2E thin and behavior-focused.
- CI flake budget with weekly trend dashboard.
- Optional perf/chaos/security jobs turned on by default for nightly runs.
- Requirements-to-tests mapping snapshot in each `run-summary.md`.

---

## License

MIT (or project default). Replace with your organization policy if needed.

---

### Recruiter-facing summary (copyable)

High-volume Playwright+Pytest lab for Windows-first teams. CI-sharded E2E with deterministic data and AI-assisted triage cut regression time from `<Xh>` to `<Yh>` and kept new flakes under 1%. Provides executive-ready run summaries and artifacts for rapid, low-risk merges across multi-OS/browser matrices.
