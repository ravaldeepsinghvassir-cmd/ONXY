import platform
import subprocess
import sys
from pathlib import Path

MIN_PYTHON = (3, 14)

def run(*args):
    print(">", " ".join(map(str, args)))
    subprocess.run(list(map(str, args)), check=True)

if sys.version_info < MIN_PYTHON:
    raise SystemExit(
        f"ONXY requires Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+; "
        f"found {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )

print(f"🍀 ONXY setup — Python {platform.python_version()}")

run(sys.executable, "-m", "pip", "install", "--upgrade", "pip")
run(sys.executable, "-m", "pip", "install", "-r", "requirements.txt")

print("Installing Playwright Chromium...")
run(sys.executable, "-m", "playwright", "install", "chromium")

if platform.system() == "Windows":
    try:
        import win32com.client  # noqa: F401
        print("pywin32: OK")
    except ImportError:
        postinstall = Path(sys.executable).parent / "Scripts" / "pywin32_postinstall.py"
        print("pywin32 import failed; continuing. If needed:")
        print(f'"{sys.executable}" -m pip install --force-reinstall pywin32')
        print(f'"{sys.executable}" "{postinstall}" -install')

print("\n✅ Setup complete. Run: python main.py")
