"""Fast Python 3.14 compatibility smoke test for ONXY."""
import sys
import py_compile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_python_version():
    assert sys.version_info >= (3, 14), sys.version

def test_compile_all():
    failures = []
    for path in ROOT.rglob("*.py"):
        if ".venv" in path.parts or "__pycache__" in path.parts:
            continue
        try:
            py_compile.compile(str(path), doraise=True)
        except Exception as exc:
            failures.append(f"{path}: {exc}")
    assert not failures, "\n".join(failures)

if __name__ == "__main__":
    test_python_version()
    test_compile_all()
    print("ONXY Python 3.14 smoke test: PASS")
