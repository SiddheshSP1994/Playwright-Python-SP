
from __future__ import annotations
import os, time, json
import httpx
from .base import AIProvider, AIResponse

# Simple price table (USD per 1K tokens). Add/adjust as needed.
PRICE = {
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o": {"input": 5.00, "output": 15.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
}

class OpenAILikeProvider(AIProvider):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("AI_API_KEY") or os.getenv("OPENAI_API_KEY", "")
        self.base_url = os.getenv("AI_BASE_URL", "https://api.openai.com/v1")
        self.model = os.getenv("AI_MODEL", self.model)

    def _estimate_cost(self, in_tok: int, out_tok: int) -> float:
        p = PRICE.get(self.model, {"input": 0.0, "output": 0.0})
        return (in_tok/1000.0)*p["input"] + (out_tok/1000.0)*p["output"]

    def chat(self, prompt: str, system: str | None = None) -> AIResponse:
        t0 = time.time()
        if not self.api_key:
            # fall back to a local no-cost response
            text = "[openai-like disabled: missing API key] " + (prompt[:200] if prompt else "")
            dt = int((time.time() - t0) * 1000)
            self.audit({"provider":"openai_like","model":self.model,"cost_usd":0.0,"latency_ms":dt,"disabled":True,"ts":time.time()})
            return AIResponse(text=text, prompt_tokens=0, completion_tokens=len(text)//4, cost_usd=0.0, latency_ms=dt)

        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {
            "model": self.model,
            "messages": ([{"role":"system","content":system}] if system else []) + [{"role":"user","content":prompt}],
            "max_tokens": self.max_tokens,
            "temperature": float(os.getenv("AI_TEMPERATURE", "0")),
        }
        # Rough pre-check: assume prompt token count as len(prompt)//4
        est_in = max(1, len(prompt)//4)
        if not self.budget.check(self._estimate_cost(est_in, self.max_tokens)):
            return AIResponse(text="[AI budget exhausted]", prompt_tokens=0, completion_tokens=0, cost_usd=0.0, latency_ms=int((time.time()-t0)*1000))

        try:
            with httpx.Client(timeout=self.timeout) as client:
                r = client.post(f"{self.base_url}/chat/completions", headers=headers, json=payload)
                r.raise_for_status()
                data = r.json()
                text = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})
                in_tok = usage.get("prompt_tokens", est_in)
                out_tok = usage.get("completion_tokens", max(1, len(text)//4))
                cost = self._estimate_cost(in_tok, out_tok)
                if not self.budget.check(cost):
                    text = "[AI budget would be exceeded by this call]"
                    cost = 0.0
                else:
                    self.budget.add(cost)
                dt = int((time.time() - t0) * 1000)
                self.audit({"provider":"openai_like","model":self.model,"cost_usd":cost,"latency_ms":dt,"usage":{"in":in_tok,"out":out_tok},"ts":time.time()})
                return AIResponse(text=text, prompt_tokens=in_tok, completion_tokens=out_tok, cost_usd=cost, latency_ms=dt)
        except Exception as e:
            dt = int((time.time() - t0) * 1000)
            self.audit({"provider":"openai_like","model":self.model,"error":str(e),"latency_ms":dt,"ts":time.time()})
            return AIResponse(text=f"[AI error] {e}", prompt_tokens=0, completion_tokens=0, cost_usd=0.0, latency_ms=dt)

def get() -> OpenAILikeProvider:
    return OpenAILikeProvider()
