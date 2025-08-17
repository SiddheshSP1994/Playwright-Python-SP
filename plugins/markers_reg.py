from __future__ import annotations
from typing import Iterable

_MARKERS: Iterable[str] = (
    "smoke: fast/high-value checks",
    "regression: broad coverage suite",
    "slow: long-running checks",
    "flaky: unstable under some conditions",
    "ai: exercises AI/LLM-assisted flows",
)

def pytest_configure(config) -> None:
    # Make markers known so pytest doesn't warn and -m works cleanly
    for m in _MARKERS:
        config.addinivalue_line("markers", m)

def pytest_addoption(parser) -> None:
    parser.addoption(
        "--allow-slow",
        action="store_true",
        default=False,
        help="Do not deselect @pytest.mark.slow tests by default",
    )

def pytest_collection_modifyitems(config, items):
    if config.getoption("--allow-slow"):
        return
    remaining, deselected = [], []
    for it in items:
        if it.get_closest_marker("slow"):
            deselected.append(it)
        else:
            remaining.append(it)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining
