from pathlib import Path

# Папки проекта
ROOT = Path(__file__).resolve().parent
SRC = Path(ROOT, "src")
DATA = Path(SRC, "data")
TESTS = Path(SRC, "tests")

# Файлы данных
OPERATIONS = Path(DATA, "operations.json")
TEST_DATA = Path(TESTS, 'test_data.json')
