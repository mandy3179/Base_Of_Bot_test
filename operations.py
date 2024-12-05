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
