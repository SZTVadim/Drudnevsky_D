
# ЗАДАЧА 1: Система учета сотрудников

employees = {

    "Иван": {"возраст": 30, "отдел": "IT", "зарплата": 80000},

    "Мария": {"возраст": 25, "отдел": "HR", "зарплата": 60000},

    "Петр": {"возраст": 35, "отдел": "ITR", "зарплата": 90000}

}

# 1. Добавьте нового сотрудника "Анна"
employees["Анна"] = {"возраст": 28, "отдел": "HR", "зарплата": 65000}
# print(employees)
# 2. Создайте список всех имен сотрудников
list1= list(employees.keys())
# print(list1)
# 3. Найдите среднюю зарплату всех сотрудников
# list2 = list(employees.values())
# print(list2)
list_zp = [zp["зарплата"] for zp in employees.values()]
salary_avg = sum(list_zp) / len(list_zp)
print(list_zp)
print(salary_avg)

# 4. Создайте множество всех отделов
lot_1 = {x["отдел"] for x in employees.values()}
print(lot_1)

# 5. Удалите сотрудника "Петр" и сохраните его данные
# name = employees.pop("Петр")
# print(name)
# 6. Создайте словарь, где ключ - отдел, а значение - список имен сотрудников
dickt_0 ={}
for name,data in employees.items():
    otdel = data["отдел"]
    dickt_0[otdel] = name
print(dickt_0)

# dict_1 = {key["отдел"]: vel[]}

