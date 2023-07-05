from pathlib import Path

# Папки проекта
ROOT = Path(__file__).resolve().parent
SRC = Path(ROOT, "src")
DATA = Path(SRC, "data")

# Файлы данных
OPERATIONS = Path(DATA, "operations.json")
