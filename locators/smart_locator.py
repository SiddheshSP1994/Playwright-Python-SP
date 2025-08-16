
from __future__ import annotations
import json, os
from pathlib import Path

from ai.providers import get_provider

SCORES_PATH = Path(os.getenv("LOCATOR_SCORES_PATH", "artifacts/locator_scores.json"))
SCORES_PATH.parent.mkdir(parents=True, exist_ok=True)

DEFAULT_STRATEGIES = ["get_by_role", "get_by_test_id", "get_by_text", "css", "xpath"]

def _load_scores():
    if SCORES_PATH.exists():
        try:
            return json.loads(SCORES_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def _save_scores(scores):
    SCORES_PATH.write_text(json.dumps(scores, indent=2), encoding="utf-8")

class SmartLocator:
    def __init__(self, page, ai_enabled: bool | None = None):
        self.page = page
        self.ai_enabled = (os.getenv("AI_ENABLED", "1") == "1") if ai_enabled is None else ai_enabled

    def find(self, target: str, strategies=None):
        strategies = strategies or DEFAULT_STRATEGIES
        scores = _load_scores()
        best = None
        for strat in strategies:
            try:
                loc = None
                if strat == "get_by_role":
                    loc = self.page.get_by_role("button", name=target)
                elif strat == "get_by_test_id":
                    loc = self.page.get_by_test_id(target)
                elif strat == "get_by_text":
                    loc = self.page.get_by_text(target, exact=True)
                elif strat == "css":
                    loc = self.page.locator(target)
                elif strat == "xpath":
                    loc = self.page.locator(f"xpath={target}")
                if loc is not None and loc.count() > 0:
                    best = loc
                    # Update score (simple +1)
                    scores[target] = scores.get(target, 0) + 1
                    break
            except Exception:
                continue
        _save_scores(scores)
        return best

    def explain(self, target: str) -> str:
        if not self.ai_enabled:
            return "[AI disabled]"
        prov = get_provider()
        prompt = f"Suggest resilient Playwright locator strategies for: {target}. Return 3 ranked ideas."
        return prov.chat(prompt, system="You are a senior test engineer. Be concise.").text
