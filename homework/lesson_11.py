# Задача 1:
cube_list = [x**3 for x in range(9)]
print(min(cube_list), max(cube_list))
# print(min([x ** 3 for x in range(9)]), max([x ** 3 for x in range(9)]))

# Задача 2:
list1 = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
list_limit = [x for x in list1 if x > 10]
print(sum(list_limit))

# Задача 3:
cities = ["москва", "санкт-петербург", "казань"]
up_cities = [city.title() for city in cities]
print(up_cities)
