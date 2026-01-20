class books:
    def __init__(self, author, page, title):
        self.title = title
        self.author = author
        self.page = int(page)

    genre = "fantasy"

    def get_info(self):
        return print(f"Название {self.title} автор {self.author}, кол.стр. {self.page}")

    def is_long(self):
        if self.page > 300:
            return print(True)
        else:
            return print(False)


book1 = books("Толкин", "600", "Властелин колец")
book2 = books("Дэн Абнетт", "299", "Возвышение Хоруса")
book3 = books("Братья Стругацкие", "320", "Страна багровых туч")

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

    type_Account = "Физическое лицо"

    def deposits(self, refill):
        self.balans += refill
        return self.balans

    def withdraw(self, expense):
        if self.balans >= expense:
            self.balans -= expense
            return print(f"Cумма сниятия {expense}  Текущий баланс: {self.balans}")
        else:
            return print(f"Недостаточно средств. Доступно {self.balans}")

    def get_balans(self):
        return print(self.balans)


my_deposits = BankAccount("Руднев Дмитрий", 6000)

print("Текущий баланс: ")
my_deposits.get_balans()

print("_______________________")

amount = int(input("Введите сумму пополнения: "))
print(f"Баланс пополнен на {amount}")
print("Текущий баланс :")
my_deposits.deposits(amount)
my_deposits.get_balans()


print("_______________________")

volue = int(input("Введите сумму  для снятия:  "))
my_deposits.withdraw(volue)


print("_______________________")
volue1 = int(input("Введите сумму  для снятия:  "))
my_deposits.withdraw(volue1)
