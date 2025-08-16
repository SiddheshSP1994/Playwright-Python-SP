
from __future__ import annotations
import os, time, json
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Env switches
AI_ENABLED = os.getenv("AI_ENABLED", "1") == "1"
AI_PROVIDER = os.getenv("AI_PROVIDER", "stub")
AI_MODEL = os.getenv("AI_MODEL", "gpt-4o-mini")
AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", "600"))
AI_TIMEOUT_SEC = int(os.getenv("AI_TIMEOUT_SEC", "30"))
AI_BUDGET_USD = float(os.getenv("AI_BUDGET_USD", "0.50"))

@dataclass
class AIResponse:
    text: str
    prompt_tokens: int = 0
    completion_tokens: int = 0
    cost_usd: float = 0.0
    latency_ms: int = 0

class Budget:
    def __init__(self, ceiling_usd: float):
        self.ceiling = max(0.0, ceiling_usd)
        self.spent = 0.0

    def check(self, planned_cost: float) -> bool:
        return (self.spent + planned_cost) <= self.ceiling + 1e-9

    def add(self, cost: float) -> None:
        self.spent += max(0.0, cost)

class AIProvider(ABC):
    def __init__(self):
        self.enabled = AI_ENABLED
        self.model = AI_MODEL
        self.max_tokens = AI_MAX_TOKENS
        self.timeout = AI_TIMEOUT_SEC
        self.budget = Budget(AI_BUDGET_USD)
        self.audit_log_path = os.getenv("AI_AUDIT_LOG", "artifacts/ai_audit.log")
        os.makedirs("artifacts", exist_ok=True)

    def redact(self, text: str) -> str:
        # lightweight redaction: mask emails and obvious tokens
        import re
        text = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "<EMAIL>", text)
        text = re.sub(r"(sk-[A-Za-z0-9]{20,})", "<TOKEN>", text)
        return text

    def audit(self, entry: dict) -> None:
        try:
            with open(self.audit_log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception:
            pass

    @abstractmethod
    def chat(self, prompt: str, system: str | None = None) -> AIResponse:
        ...
