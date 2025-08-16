
from __future__ import annotations
import math, re
from pathlib import Path

KB_DIR = Path("docs/kb")
KB_DIR.mkdir(parents=True, exist_ok=True)

def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9]+", text.lower())

def _vec(text: str) -> dict[str,int]:
    v = {}
    for t in _tokenize(text):
        v[t] = v.get(t, 0) + 1
    return v

def _cos(a: dict[str,int], b: dict[str,int]) -> float:
    dot = sum(a.get(k,0)*b.get(k,0) for k in set(a)|set(b))
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na*nb>0 else 0.0

def search(query: str, k: int = 3):
    qv = _vec(query)
    results = []
    for p in KB_DIR.glob("**/*.md"):
        s = p.read_text(encoding="utf-8", errors="ignore")
        score = _cos(qv, _vec(s))
        results.append((score, p))
    results.sort(reverse=True)
    return results[:k]
