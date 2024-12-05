from models import Book
from storage import load_data, save_data


def add_book(title: str, author: str, year: int) -> None:
    """
    Добавляет новую книгу в библиотеку.

    Args:
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
    """
    data = load_data()
    new_id = max((book.id for book in data), default=0) + 1
    new_book = Book(
        book_id=new_id,
        title=title,
        author=author,
        year=year
    )
    data.append(new_book)
    save_data(data)
    print(f"Книга '{title}' добавлена с ID {new_id}.")


def delete_book(book_id: int) -> None:
    """
    Удаляет книгу из библиотеки по её уникальному идентификатору (ID).

    Args:
        book_id (int): Уникальный идентификатор книги, которую нужно удалить.
    """
    data = load_data()
    book = next((b for b in data if b.id == book_id), None)

    if not book:
        print("Ошибка: книга с таким ID не найдена.")
        return

    data.remove(book)
    save_data(data)
    print(f"Книга с ID {book_id} удалена.")


def search_books(query: str, field: str) -> None:
    """
    Ищет книги в библиотеке по указанному полю и запросу.

    Args:
        query (str): Поисковый запрос.
        field (str): Поле для поиска. Доступны значения: "title", "author", "year".
    """
    data = load_data()
    field_map = {
        "title": "title",
        "author": "author",
        "year": "year"
    }
    if field not in field_map:
        print("Ошибка: некорректное поле для поиска.")
        return

    results = [b for b in data if query.lower() in str(getattr(b, field)).lower()]

    if not results:
        print("Книги не найдены.")
        return

    display_books(results)


def display_books(books: list[Book] = None) -> None:
    """
    Выводит список книг в библиотеке или переданный список книг.

    Args:
        books (list[Book], optional): Список объектов Book для отображения. 
                                    Если не указан, загружаются все книги из библиотеки.
    """
    data = books if books else load_data()
    if not data:
        print("Библиотека пуста.")
        return

    for book in data:
        print(
            f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
            f"Год: {book.year}, Статус: {book.status}"
        )


def update_status(book_id: int, status: str) -> None:
    """
    Обновляет статус книги по её уникальному идентификатору (ID).

    Args:
        book_id (int): Уникальный идентификатор книги.
        status (str): Новый статус книги. Доступны значения: "в наличии", "выдана".
    """
    if status not in ["в наличии", "выдана"]:
        print("Ошибка: недопустимый статус.")
        return

    data = load_data()
    book = next((b for b in data if b.id == book_id), None)

    if not book:
        print("Ошибка: книга с таким ID не найдена.")
        return

    book.status = status
    save_data(data)
    print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
