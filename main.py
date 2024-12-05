from operations import (
    add_book,
    delete_book,
    search_books,
    display_books,
    update_status
)


def main() -> None:
    """Основная функция для работы с приложением."""
    while True:
        print("\nУправление библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        try:
            if choice == "1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год издания: "))
                add_book(title, author, year)
            elif choice == "2":
                book_id = int(input("Введите ID книги: "))
                delete_book(book_id)
            elif choice == "3":
                field = input("Введите поле для поиска (title, author, year): ")
                query = input("Введите запрос: ")
                search_books(query, field)
            elif choice == "4":
                display_books()
            elif choice == "5":
                book_id = int(input("Введите ID книги: "))
                status = input("Введите новый статус ('в наличии' или 'выдана'): ")
                update_status(book_id, status)
            elif choice == "6":
                print("Выход из программы.")
                break
            else:
                print("Ошибка: некорректный выбор.")
        except ValueError:
            print("Ошибка: некорректный ввод.")

if __name__ == "__main__":
    main()
