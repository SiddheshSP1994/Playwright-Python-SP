from __future__ import annotations
import os
import sys
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts"
HTML_DIR = ROOT / "playwright-report"
HTML_REPORT = HTML_DIR / "report.html"
ALLURE_DIR = ROOT / "allure-results"

for p in (ART, HTML_DIR, ALLURE_DIR):
    p.mkdir(parents=True, exist_ok=True)

RUN_SUITE = os.getenv("RUN_SUITE", "smoke").lower()  # smoke | full
BROWSER = os.getenv("BROWSER", "chromium")
AI_ENABLED = os.getenv("AI_ENABLED", "0") == "1"

PY = sys.executable  # always use the same interpreter that launched this script

def run_pytest(extra_args: list[str]) -> int:
    cmd = [
        PY, "-m", "pytest", "-q",
        f"--browser={BROWSER}",
        f"--html={HTML_REPORT}",
        "--self-contained-html",
        f"--alluredir={ALLURE_DIR}",
    ]
    if RUN_SUITE == "smoke":
        cmd += ["-m", "smoke"]
    if AI_ENABLED:
        cmd += ["-p", "plugins.ai_triage", "--ai-triage"]
    cmd += extra_args
    print("RUN:", " ".join(cmd), flush=True)
    return subprocess.call(cmd, cwd=str(ROOT))

def collect_failures() -> list[str]:
    cache = ROOT / ".pytest_cache" / "v" / "cache" / "lastfailed"
    if not cache.exists():
        return []
    try:
        return list(json.loads(cache.read_text()).keys())
    except Exception:
        return []

def write_stub_triage_md(first: list[str], remaining: list[str]) -> None:
    md = ART / "ai-triage.md"
    lines = [
        "# Failure Triage (stub)",
        f"- Suite: {RUN_SUITE}",
        f"- Browser: {BROWSER}",
        f"- First run failures: {len(first)}",
        f"- After rerun failures: {len(remaining)}",
        "",
        "## Remaining failing tests",
    ]
    for nid in remaining:
        lines.append(f"- `{nid}`")
    md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {md}")

# First pass
exit1 = run_pytest([])
first = collect_failures()

# One rerun for failed nodes (flake filter)
exit2 = 0
remaining = first
if first:
    exit2 = run_pytest(first)
    remaining = collect_failures()

if not AI_ENABLED:
    write_stub_triage_md(first, remaining)
else:
    print("AI triage handled by plugins.ai_triage")

sys.exit(exit1 or exit2)
