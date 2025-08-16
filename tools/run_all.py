# tools/run_all.py
from __future__ import annotations
import os, sys, time, socket, atexit, multiprocessing as mp
from pathlib import Path

PAY_HOST, PAY_PORT = "127.0.0.1", int(os.getenv("PAY_PORT", "8081"))
MAIL_HOST, MAIL_PORT = "127.0.0.1", int(os.getenv("MAIL_PORT", "8082"))

def wait_port(host: str, port: int, timeout: float = 90.0) -> None:
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            with socket.create_connection((host, port), timeout=1.0):
                return
        except OSError:
            time.sleep(0.2)
    raise RuntimeError(f"Port {host}:{port} not ready after {timeout}s")

def run_uvicorn_import(import_str: str, host: str, port: int) -> None:
    # Ensure project root (parent of tools/) is on sys.path
    root = Path(__file__).resolve().parent.parent
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

    import uvicorn
    # Pass import string (picklable) instead of app object
    uvicorn.run(import_str, host=host, port=port, log_level="info")

def start_fakes() -> list[mp.Process]:
    procs: list[mp.Process] = []
    # Start payment and mail fakes via import strings
    for import_str, host, port in (
        ("services.fakes.payment_gateway.app:app", PAY_HOST, PAY_PORT),
        ("services.fakes.mail.app:app",           MAIL_HOST, MAIL_PORT),
    ):
        p = mp.Process(target=run_uvicorn_import, args=(import_str, host, port), daemon=True)
        p.start()
        procs.append(p)

    # Wait until both ports are reachable
    wait_port(PAY_HOST, PAY_PORT, timeout=90)
    wait_port(MAIL_HOST, MAIL_PORT, timeout=90)
    return procs

def main() -> int:
    os.environ.setdefault("TEST_ENV", "default")
    os.environ.setdefault("PAYMENTS_FAKE_URL", f"http://{PAY_HOST}:{PAY_PORT}")
    os.environ.setdefault("MAIL_FAKE_URL", f"http://{MAIL_HOST}:{MAIL_PORT}")

    procs: list[mp.Process] = []
    def cleanup():
        for p in procs:
            if p.is_alive():
                p.terminate()
                p.join(timeout=5)
    atexit.register(cleanup)

    procs[:] = start_fakes()

    try:
        import pytest
    except ImportError:
        print("pytest not installed. Run: pip install -r requirements.txt", file=sys.stderr)
        return 1

    # ensure report dir exists
    report_dir = Path("reports")
    report_dir.mkdir(parents=True, exist_ok=True)
    return pytest.main([
        "-n", "auto", "--maxfail=1",
        "--alluredir", "allure-results",
        "--html", str(report_dir / "pytest-report.html"), "--self-contained-html",
        "--junitxml", "reports/junit.xml",
    ])

if __name__ == "__main__":
    mp.freeze_support()  # required on Windows
    sys.exit(main())
