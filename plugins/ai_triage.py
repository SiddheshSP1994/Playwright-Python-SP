
from __future__ import annotations
import os, json, traceback, hashlib
from pathlib import Path
from datetime import datetime

from ai.providers import get_provider
from ai.registry import get_prompt

ART_DIR = Path(os.getenv("ARTIFACTS_DIR", "artifacts"))
ART_DIR.mkdir(parents=True, exist_ok=True)
JSON_PATH = ART_DIR / "ai_triage.json"
MD_PATH = ART_DIR / "ai-triage.md"

_failures = []

def _sig(item) -> str:
    # hash on location + message head for clustering
    msg = item.get("error", "")[:200]
    loc = item.get("nodeid", "")
    return hashlib.sha1((loc + "|" + msg).encode("utf-8")).hexdigest()[:10]

def pytest_addoption(parser):
    group = parser.getgroup("ai_triage")
    group.addoption("--ai-triage", action="store_true", default=False, help="Enable AI triage summary on sessionfinish")

def pytest_runtest_makereport(item, call):
    # Collect failure info
    if call.when == "call":
        rep = call.excinfo
        if rep is not None:
            err = "".join(traceback.format_exception(rep.type, rep.value, rep.tb))
            # Try to find last screenshot or trace
            # Common Playwright outputs
            screenshot = None
            trace = None
            candidates = [
                Path("playwright-report"), Path("test-results"), Path("reports"), Path("artifacts")
            ]
            for base in candidates:
                if base.exists():
                    for p in base.rglob("*"):
                        name = p.name.lower()
                        if screenshot is None and name.endswith((".png",".jpg",".jpeg","screenshot.png")):
                            screenshot = str(p)
                        if trace is None and ("trace.zip" in name or name.endswith(".zip") and "trace" in name):
                            trace = str(p)
            _failures.append({
                "nodeid": item.nodeid,
                "error": err,
                "screenshot": screenshot,
                "trace": trace,
            })

def pytest_sessionfinish(session, exitstatus):
    if not _failures:
        # write empty files to keep CI predictable
        JSON_PATH.write_text(json.dumps({"failures": [], "generated_at": datetime.utcnow().isoformat()+"Z"}, indent=2), encoding="utf-8")
        MD_PATH.write_text("# AI Triage\n\nNo failures.\n", encoding="utf-8")
        return

    # cluster by signature
    clusters = {}
    for f in _failures:
        k = _sig(f)
        clusters.setdefault(k, []).append(f)

    data = {
        "generated_at": datetime.utcnow().isoformat()+"Z",
        "count": len(_failures),
        "clusters": [{"id": k, "size": len(v), "samples": v[:3]} for k,v in clusters.items()],
    }
    JSON_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # Compose context for AI
    enable = os.getenv("AI_ENABLED", "1") == "1"
    use_ai = enable and os.getenv("AI_PROVIDER", "stub") in ("stub","openai","openai_like","openai-like")
    header = f"# AI Triage\n\nFailures: {len(_failures)} in {len(clusters)} cluster(s)\n\n"
    body = ""
    if use_ai and session.config.getoption("--ai-triage", default=False):
        prov = get_provider()
        prompt = get_prompt("triage")
        context = json.dumps(data, ensure_ascii=False)
        # Keep prompt small-ish
        combined = f"{prompt}\n\nContext:\n{context[:60000]}"
        resp = prov.chat(combined, system="You are a strict, concise test triage assistant.")
        body = resp.text
    else:
        # Deterministic fallback summary
        for k, v in clusters.items():
            head = v[0]["error"].splitlines()[:3]
            body += f"## Cluster {k} (size {len(v)})\n"
            body += "````\n" + "\n".join(head) + "\n````\n\n"
            body += "- Hints: check selectors, waits, and recent commits touching affected pages.\n\n"

    # Write markdown
    MD_PATH.write_text(header + body + "\n", encoding="utf-8")
