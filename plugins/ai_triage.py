import os
import re
import pathlib
from collections import defaultdict
import pytest

ART = pathlib.Path("artifacts")
ART.mkdir(parents=True, exist_ok=True)

KEY_HINTS = [
    (re.compile(r"timeout|timed out|waiting for", re.I), "Wait/selector stability: use explicit waits or stabilize network/fixtures."),
    (re.compile(r"locator|no such element|selector", re.I), "Selector robustness: prefer role-based locators and stable attributes."),
    (re.compile(r"AssertionError", re.I), "Expectation mismatch: verify test data and assertions."),
    (re.compile(r"\b5\d{2}\b|ECONN|network", re.I), "Service dependency: fake/stub backend or retry with backoff."),
    (re.compile(r"TypeError|KeyError|AttributeError", re.I), "Test/page-object bug: add guards, null checks, or fix data shape."),
]

def _longrepr_text(rep):
    try:
        return rep.longreprtext  # pytest >=6
    except Exception:
        try:
            return str(rep.longrepr)
        except Exception:
            return "unknown error"

def _signature(msg: str) -> str:
    # Normalize: lowercase, strip variable bits (numbers/uuids), take first 160 chars
    norm = msg.lower()
    norm = re.sub(r"[0-9a-f]{8,}", "<id>", norm)  # crude uuid/hash mask
    norm = re.sub(r"\d+", "<n>", norm)
    return norm[:160]

def _hint_for(msg: str) -> str:
    for pat, hint in KEY_HINTS:
        if pat.search(msg):
            return hint
    return "Generic: check recent diffs, data seeding, and page object contracts."

class AITriagePlugin:
    def __init__(self, config: pytest.Config):
        self.enabled = bool(config.getoption("--ai-triage")) or os.getenv("AI_ENABLED", "0") == "1"
        self.provider = os.getenv("AI_PROVIDER", "stub")
        self.failures = []

    @pytest.hookimpl
    def pytest_runtest_logreport(self, report: pytest.TestReport):
        if not self.enabled:
            return
        if report.when == "call" and report.failed:
            msg = _longrepr_text(report)
            self.failures.append({
                "nodeid": report.nodeid,
                "message": msg,
            })

    @pytest.hookimpl
    def pytest_sessionfinish(self, session: pytest.Session, exitstatus: int):
        if not self.enabled:
            return
        clusters = defaultdict(list)
        for f in self.failures:
            sig = _signature(f["message"])
            clusters[sig].append(f)

        lines = [
            "# AI Triage (provider: stub)",
            f"- Enabled: {self.enabled}",
            f"- Failures observed: {len(self.failures)}",
            f"- Clusters: {len(clusters)}",
            "",
        ]
        for i, (sig, items) in enumerate(clusters.items(), 1):
            sample_msg = items[0]["message"].splitlines()[0][:200]
            lines += [
                f"## Cluster {i}  — {len(items)} tests",
                f"**Signature:** `{sig}`",
                f"**Hypothesis:** {_hint_for(sample_msg)}",
                "",
                "**Examples:**",
            ]
            for it in items[:10]:
                lines.append(f"- `{it['nodeid']}`")
            lines.append("")
            lines.append("<details><summary>Sample message</summary>\n\n```\n" + sample_msg + "\n```\n</details>\n")

        out = ART / "ai-triage.md"
        out.write_text("\n".join(lines), encoding="utf-8")
        session.config.pluginmanager.get_plugin("terminalreporter").write_line(f"AI triage: wrote {out}")

def pytest_addoption(parser: pytest.Parser):
    group = parser.getgroup("ai-triage")
    group.addoption("--ai-triage", action="store_true", default=False, help="Enable AI-assisted failure triage (stub provider)")

def pytest_configure(config: pytest.Config):
    config.pluginmanager.register(AITriagePlugin(config), name="ai-triage-plugin")
