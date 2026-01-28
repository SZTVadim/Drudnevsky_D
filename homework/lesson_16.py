class Book:
    def __init__(self, author, pages, title):
        self.title = title
        self.author = author
        self.pages = int(pages)

    genre = "fantasy"

    def get_info(self):
        return f"Название {self.title} автор {self.author}, кол.стр. {self.pages}"

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False


book1 = Book("Толкин", "600", "Властелин колец")
book2 = Book("Дэн Абнетт", "299", "Возвышение Хоруса")
book3 = Book("Братья Стругацкие", "320", "Страна багровых туч")

book1.get_info()
book2.get_info()
book3.get_info()

book1.is_long()
book2.is_long()
book3.is_long()


class BankAccount:
    def __init__(self, owner, balans=0):
        self.owner = owner
        self.balans = balans

    client_type = "Физическое лицо"

    def deposit(self, refill):
        self.balans += refill
        return self.balans

    def withdraw(self, expense):
        if self.balans >= expense:
            self.balans -= expense
            return f"{True}  Текущий баланс: {self.balans}"
        else:
            return f"{False} Недостаточно средств "

    def get_balance(self):
        return self.balans


my_deposits = BankAccount("Руднев Дмитрий", 1000)


print(my_deposits.get_balance())
print(my_deposits.deposit(5000))
print(my_deposits.get_balance())
print(my_deposits.withdraw(3000))
print(my_deposits.withdraw(6000))
