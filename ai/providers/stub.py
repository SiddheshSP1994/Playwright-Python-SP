
from __future__ import annotations
import time
from .base import AIProvider, AIResponse

class StubProvider(AIProvider):
    def chat(self, prompt: str, system: str | None = None) -> AIResponse:
        t0 = time.time()
        # Deterministic pseudo-summary
        summary = (prompt or "").strip().replace("\n", " ")
        if len(summary) > 240:
            summary = summary[:240] + "..."
        text = f"[STUB AI]\nSystem={system or 'none'}\nSummary={summary}"
        dt = int((time.time() - t0) * 1000)
        resp = AIResponse(text=text, prompt_tokens=len(prompt)//4, completion_tokens=len(text)//4, cost_usd=0.0, latency_ms=dt)
        self.audit({"provider": "stub", "model": self.model, "cost_usd": 0.0, "latency_ms": dt, "ts": time.time()})
        return resp

def get() -> StubProvider:
    return StubProvider()
