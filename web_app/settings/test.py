from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

FIXTURE_DIRS = [f"{BASE_DIR}/tests/fixtures"]

# [TODO](mtt): Add user connection timeout
