
from __future__ import annotations
import subprocess, sys, os
from pathlib import Path

def git_changed_files(base: str = "origin/main") -> list[str]:
    try:
        out = subprocess.check_output(["git", "diff", "--name-only", f"{base}...HEAD"], text=True)
        return [l.strip() for l in out.splitlines() if l.strip()]
    except Exception:
        return []

def map_to_tests(paths: list[str]) -> list[str]:
    tests = []
    for p in paths:
        if p.startswith("tests") and p.endswith(".py"):
            tests.append(p)
        # Heuristic: page or app code touched -> run all tests (could be smarter with coverage map)
    return sorted(set(tests))

def main():
    base = os.getenv("TIA_BASE", "origin/main")
    changed = git_changed_files(base)
    tests = map_to_tests(changed)
    out = Path("artifacts/test_selection.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    if tests:
        out.write_text("\n".join(tests), encoding="utf-8")
        print(f"[TIA] Selected {len(tests)} test file(s). Saved to {out}.")
    else:
        out.write_text("", encoding="utf-8")
        print("[TIA] No specific tests selected. Run full suite.")

if __name__ == "__main__":
    main()
