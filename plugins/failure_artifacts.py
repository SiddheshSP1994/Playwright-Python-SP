import os
import random
import time
import pathlib
import pytest

SEED = int(os.getenv("SEED", "42"))
random.seed(SEED)

ARTIFACTS_DIR = pathlib.Path("artifacts")
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when != "call" or rep.passed:
        return
    page = item.funcargs.get("page")
    if not page:
        return
    safe = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
    ts = int(time.time())
    png = ARTIFACTS_DIR / f"{safe}_{ts}.png"
    html = ARTIFACTS_DIR / f"{safe}_{ts}.html"
    try:
        page.screenshot(path=str(png), full_page=True)
    except Exception:
        pass
    try:
        html.write_text(page.content(), encoding="utf-8")
    except Exception:
        pass
