import argparse
import json
from pathlib import Path


def update_values(values: dict[int, str], test: dict):

    if "value" in test:
        test["value"] = values[test["id"]]
    if "values" in test:
        for item in test["values"]:
            update_values(values, item)


def create_report(
    values_path: Path = Path("./values.json"),
    tests_path: Path = Path("./tests.json"),
    report_path: Path = Path("./report.json"),
):

    # Загружаем данные из values.json
    with open(values_path, "r") as file:
        values = json.load(file)

    # Загружаем данные из tests.json
    with open(tests_path, "r") as file:
        tests = json.load(file)

    # Создаем словарь для быстрого поиска значений по id
    values = {value["id"]: value["value"] for value in values["values"]}

    # Сопоставление результатов тестов с их id и заполнение структуры отчета
    for item in tests["tests"]:
        update_values(values, item)

    # Сохранение обновленной структуры отчета в report.json
    with open(report_path, "w") as report:
        json.dump(tests, report, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Создание отчета на основе JSON файлов")
    parser.add_argument("-v", type=Path, help="Путь к файлу", default="values.json")
    parser.add_argument("-t", type=Path, help="Путь к файлу", default="tests.json")
    parser.add_argument("-r", type=Path, help="Путь для сохранения", default="report.json")
    args = parser.parse_args()

    if not args.v.exists():
        print(f"Файл {args.v} не найден")

    if not args.t.exists():
        print(f"Файл {args.t} не найден")

    create_report(args.v, args.t, args.r)

    if args.r.exists():
        print(f"Файл {args.r} успешно создан/обновлен")
