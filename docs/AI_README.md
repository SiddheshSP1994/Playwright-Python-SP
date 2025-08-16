
# AI & Triage Additions

Generated: 2025-08-16T14:43:42.923383Z

## Quick start

```bash
# Windows (Git Bash / PowerShell)
set AI_ENABLED=1
set AI_PROVIDER=stub
pytest -q --ai-triage
```

- Markdown summary: `artifacts/ai-triage.md`
- JSON data: `artifacts/ai_triage.json`

## Providers
- **stub**: deterministic, offline, zero-cost
- **openai-like**: any OpenAI-compatible endpoint via `AI_BASE_URL`, `AI_API_KEY`, `AI_MODEL`

## Budget & Policy
- `AI_BUDGET_USD` ceiling (default 0.50). Calls are skipped if exceeded.

## Self-healing locators
Use `locators.smart_locator.SmartLocator(page).find("Login")`.

## TIA (Test Impact Analysis)
CI runs `tools/tia.py` to select impacted tests first.

## Telemetry
Optional OpenTelemetry. Set `OTEL_EXPORTER_OTLP_ENDPOINT` to enable.
