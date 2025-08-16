# Enterprise Playwright + Pytest Lab (1000‑file preload)

This repository provides an example of how a larger team can structure, scale and run high‑volume end‑to‑end and API testing using **Python**, **Pytest** and **Playwright**.  It demonstrates patterns that are common in enterprise test automation projects: Page Object models, parametrised test generation, service fakes, requirements traceability and continuous integration.  A thousand generated test modules (≈10 000 parametrised cases) are included under `tests/generated/` to simulate the volume produced by many months of teamwork.

## Key features

* **Playwright with Pytest:** UI tests use Playwright’s synchronous API, driven through reusable fixtures in `conftest.py`.
* **Parametrised test suites:** Under `tests/generated/` you’ll find six suites – `checkout`, `catalog`, `orders`, `payments`, `email` and `analytics` – each broken into many files.  Each file contains 10 `@pytest.mark.parametrize` cases with structured data (SKU, quantity, coupon, etc.).  In total there are **1000 test modules** and **10 000 test cases**.
* **Service fakes:** Simple FastAPI apps in `services/fakes/payment_gateway` and `services/fakes/mail` simulate external dependencies.  They return dummy responses so you can exercise complete flows without calling real systems.
* **Multi‑environment configuration:** Although only one default environment is defined, the layout leaves room for YAML/`.env` based configuration per target environment.
* **Requirements traceability:** `docs/rtm_matrix.md` maps epics to ranges of test IDs so you can trace coverage across suites.
* **GitHub Actions CI:** The workflow in `.github/workflows/ci.yml` installs dependencies, runs Playwright tests on both Ubuntu and Windows against multiple browsers, and uploads Allure results as build artefacts.  The matrix includes 10 shards for parallelisation.

## Getting started

### Prerequisites

* Python 3.9 or later
* [Playwright](https://playwright.dev/python/) and its browser binaries (installed automatically by `python -m playwright install`)
* [Allure Commandline](https://docs.qameta.io/allure/) (optional, for viewing reports)

### Local run (Windows example)

```powershell
cd enterprise-playwright-pytest-lab-1000
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install

# Optionally start service fakes in separate terminals:
python services\fakes\payment_gateway\app.py
python services\fakes\mail\app.py

pytest -n auto --maxfail=1 --alluredir=allure-results
```

## Contributing & extension

This repository is intended as a starting point.  To extend it for your own needs you might:

* Add real page object classes in `pages/` and refactor tests to call them instead of using inline assertions.
* Introduce environment‑specific configuration via YAML and environment variables.
* Integrate [pytest‑repeat](https://pypi.org/project/pytest-repeat/) or [pytest‑rerunfailures](https://pypi.org/project/pytest-rerunfailures/) to handle flaky tests.
* Build out the `tools/generate_tests.py` script to generate test modules dynamically from your own catalogues.

Happy testing!