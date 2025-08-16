from __future__ import annotations
import os, random, time as _time, typing as _t
import pytest
from faker import Faker

@pytest.fixture(scope="session", autouse=True)
def global_seed() -> int:
    seed_env = os.getenv("TEST_SEED")
    seed = int(seed_env) if seed_env and seed_env.isdigit() else 1337
    random.seed(seed)
    Faker.seed(seed)
    return seed

@pytest.fixture(scope="session")
def fake() -> Faker:
    return Faker()

@pytest.fixture(autouse=True)
def forbid_time_sleep(monkeypatch: pytest.MonkeyPatch):
    # Default OFF to avoid breaking existing tests; enable via env when ready.
    if os.getenv("ENFORCE_NO_SLEEP", "0") != "1":
        return
    def _no_sleep(seconds: _t.Any) -> None:
        raise AssertionError(f"time.sleep({seconds}) is forbidden. Use explicit waits instead.")
    monkeypatch.setattr(_time, "sleep", _no_sleep)

@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str:
    # Use pytest-playwright's built-in --base-url if present; else fallback to env or default.
    val = None
    try:
        val = pytestconfig.getoption("--base-url")
    except Exception:
        val = None
    if not val:
        val = os.getenv("BASE_URL", "http://localhost:8000")
    return val if isinstance(val, str) else str(val)
