# ЗАДАНИЕ 1: Работа со словарями и перебор элементов
students = {"name": "Иван", "age": "20", "level": "20", "city": "Москва"}

print(students["name"])
print(students["age"])
print(students["level"])
print(students["city"])

for key in students:
    print(key)

for value in students.values():
    print(value)

for key in students.items():
    print(key)

# ЗАДАНИЕ 2: Удаление элементов и генератор словарей

prices = {
    "Яблоко": "50",
    "Банан": "30",
    "Апельсин": "40",
    "Груша": "35",
    "Виноград": "60",
}

del prices["Груша"]

grape = prices.pop("Виноград")
print(f" Удаленный ключ: {grape}")
#  {ключ: значение for элемент in итерируемый_объект}
sell_prices = {price: float(value) * 0.9 for price, value in prices.items()}
print(f" Словарь sell_prices: {sell_prices}")

# ЗАДАНИЕ 3: Объединение словарей
student1 = {"имя": "Иван", "возраст": "20", "курс": "2"}
student2 = {"имя": "Мария", "возраст": "21", "город": "Сантк-Петербург"}

student3 = student1 | student2  # создаю словарь объедения 1 и 2 но не меняя их
student1.update(student2)
print(f" Словарь student1: {student1}")
print(f" Словарь student2: {student2}")
print(f" Словарь student3: {student3}")
