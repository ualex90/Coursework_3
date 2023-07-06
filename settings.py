from pathlib import Path

# Папки проекта
ROOT = Path(__file__).resolve().parent
SRC = Path(ROOT, "src")
DATA = Path(SRC, "data")

# Файлы данных
OPERATIONS = Path(DATA, "operations.json")
TEST_DATA = Path(DATA, 'test_data.json')
