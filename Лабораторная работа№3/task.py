class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f'Количество страниц не может быть отрицательным')
        else:
            raise ValueError(f"Количество страниц должно быть представлено в виде целочисленного типа данных ")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self.duration = duration
            else:
                raise AttributeError(f'Продолжительность не может быть отрицательной')
        else:
            raise ValueError(f"Продолжительность дожна быть представлена в виде числа с плавующей зпт")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"
