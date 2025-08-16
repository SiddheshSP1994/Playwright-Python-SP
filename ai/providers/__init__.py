
from __future__ import annotations
import os
from .base import AI_ENABLED, AI_PROVIDER
from . import stub, openai_like

def get_provider():
    if not AI_ENABLED:
        return stub.get()
    prov = os.getenv("AI_PROVIDER", AI_PROVIDER).lower()
    if prov in ("openai", "openai_like", "openai-like"):
        return openai_like.get()
    return stub.get()
