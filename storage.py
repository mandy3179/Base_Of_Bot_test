import json
import os

from models import Book


DATA_FILE = "library_data.json"


def load_data() -> list[Book]:
    """
    Загружает данные из файла и возвращает список объектов Book.

    Если файл отсутствует, он создается пустым.

    Returns:
        list[Book]: Список объектов Book.
    """
    if not os.path.exists(DATA_FILE):
        save_data([])

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Book.from_dict(item) for item in data]


def save_data(data: list[Book]) -> None:
    """
    Сохраняет список объектов Book в файл.

    Args:
        data (list[Book]): Список объектов Book для сохранения.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [book.to_dict() for book in data],
            file,
            indent=4,
            ensure_ascii=False
        )
