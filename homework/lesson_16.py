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

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())

print(book1.is_long())
print(book2.is_long())
print(book3.is_long())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    client_type = "Физическое лицо"

    def deposit(self, refill):
        self.balance += refill
        return self.balance

    def withdraw(self, expense):
        if self.balance >= expense:
            self.balance -= expense
            return True
        else:
            return False
    def get_balance(self):
        return self.balance


my_deposits = BankAccount("Руднев Дмитрий", 1000)


print(my_deposits.get_balance())
print(my_deposits.deposit(5000))
print(my_deposits.get_balance())
print(my_deposits.withdraw(3000))
print(my_deposits.withdraw(6000))
