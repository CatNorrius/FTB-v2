import json
import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent / "data"

def load_json(filename):
    """Загружает JSON-файл и возвращает данные в виде словаря."""
    file_path = DATA_PATH / filename
    if file_path.exists():
        with open(file_path, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    """Сохраняет данные в JSON-файл."""
    file_path = DATA_PATH / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_csv(filename):
    """Загружает CSV-файл и возвращает список словарей."""
    file_path = DATA_PATH / filename
    if file_path.exists():
        with open(file_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    return []

# Тестовое чтение файлов
if __name__ == "__main__":
    print("Buildings:", load_csv("buildings.csv"))
    print("Recipes:", load_csv("recipes.csv"))
    print("Save:", load_json("save.json"))
