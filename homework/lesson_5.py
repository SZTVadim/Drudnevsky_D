# ЗАДАНИЕ 1: Работа с типами данных
string = "Привет"
integer = 42
floating = 3.14
list1 = [1, 2, 3]
print(type(string))
print(type(integer))
print(type(floating))
print(type(list1))

# ЗАДАНИЕ 2: Преобразование регистра строк
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

# ЗАДАНИЕ 3: Удаление пробелов
text2 = "  Hello World   "
print(text2.strip())
print(text2.lstrip())
print(text2.rstrip())

# ЗАДАНИЕ 4:Разделение и объединение строк
test3 = "яблоко,банан,апельсин,груша"
fruits = test3.split(",")
text3 = " | ".join(fruits)
print(text3)

# ЗАДАНИЕ 5: Замена подстрок
text4 = "Я изучаю Python. Python - это круто!"
print(text4.replace("Python", "Java"))

# ЗАДАНИЕ 6: Поиск и подсчет
test5 = "Python программирование на Python"
print(test5.find("Python"))
print(test5.count("Python"))
print(test5.find("Java"))

# ЗАДАНИЕ 7: Проверка типа символов

line1 = "Hello123"
line2 = "12345"
line3 = "Hello"
line4 = "    "

print(line1.isalnum())
print(line2.isdigit())
print(line3.isalpha())
print(line4.isspace())

# ЗАДАНИЕ 8: Срезы строк

line4 = "Python very good"
print(line4[:3])
print(line4[-3:])
print(line4[::2])
print(line4[::-1])

# ЗАДАНИЕ 9: Экранирование символов

line5 = 'Он сказал: "Привет"'
print(line5)
line6 = "Первая строка \nВторая строка"
print(line6)

# ЗАДАНИЕ 10: Добавление элементов в список

fruits = ["яблоко"]
fruits.append("банан")
fruits.extend(["апельсин", "грушка"])
print(fruits)
fruits.insert(1, "виноград")
print(fruits)

# ЗАДАНИЕ 11: Удаление элементов из списка
fruits = ["яблоко", "банан", "апельсин", "банан"]
print(fruits)
fruits.remove("банан")
print(fruits)
delpop = fruits.pop()
print(delpop)

# ЗАДАНИЕ 12: Поиск элементов в списке

fruits_list = ["яблоко", "банан", "апельсин", "банан"]
print(fruits_list.index("банан"))
print(fruits_list.count("банан"))

# ЗАДАНИЕ 13: Сортировка и реверс списка

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# БОНУСНОЕ 14: Комбинированная задача

name = "Иван,Петр,Мария,Анна"
name_list = name.split(",")
name_list.append("Ольга")
name_list.sort()
print(name_list)
new_name_list = ", ".join(name_list)
print(new_name_list)
