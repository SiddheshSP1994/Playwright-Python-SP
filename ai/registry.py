
from __future__ import annotations
import os
from pathlib import Path

PROMPT_VERSION = os.getenv("PROMPT_VERSION", "2025.08.16")
PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"

def get_prompt(name: str) -> str:
    p = PROMPTS_DIR / f"{name}.md"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return ""
