# Домашнее задание: Декораторы, @property и @classmethod
# ЗАДАНИЕ 1: Декоратор

# 1) Создайте декоратор log_execution:


def log_execution(fanc):
    def wrapper(a, b):
        print("Функция запущена")
        ruslt = fanc(a, b)
        print(ruslt)
        print("Функция завершена")
        return ruslt

    return wrapper


# 2) Примените декоратор к функции calculate_sum(a, b):


@log_execution
def calculate_sum(a: int, b: int):

    return a + b


result = calculate_sum(1, 2)


# ЗАДАНИЕ 2: @property и @classmethod
#
# Создайте класс Book (Книга):


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, _price):
        if _price < 0:
            print("Ошибка: цена не может быть отрицательной!")
        elif _price > 10000:
            print("Ошибка: максимальная цена 10000 рублей!")
        else:
            self._price = _price

    @classmethod
    def create_from_string(cls, line: str):

        parts = line.split("|", 1)
        title, author = parts
        return cls(title=title.split(), author=author.strip())

    def get_info(self):
        print(f"Книга  {self.title} автор {self.author}, цена {self.price}")


# print(Book.create_from_string("Война и мир|Толстой"))
book1 = Book("1984", "Оруэлл")
book2 = Book.create_from_string("Мастер и Маргарита | Булгаков")
book1.price = 500
book2.price = 750

book1.get_info()

book2.get_info()


book1.price = -100

book1.get_info()


book1.price = 15000
book1.get_info()
