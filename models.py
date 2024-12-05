class Book:
    """
    Класс для представления книги.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания книги.
        status (str): Статус книги ('в наличии' или 'выдана').
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = 'в наличии'):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """
        Преобразует объект книги в словарь.

        Returns:
            dict: Словарь с данными книги.
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: dict) -> 'Book':
        """
        Создает объект книги из словаря.

        Args:
            data (dict): Словарь с данными книги.

        Returns:
            Book: Новый объект книги.
        """
        return Book(
            book_id=data['id'],
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status']
        )
