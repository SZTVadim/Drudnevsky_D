# Задача_1:
list1 = [n ** 3 for n in range(1, 9)]
print(list1)
print(max(list1))
print(min(list1))

# Задача 2:
list2 = [5, 12, 8, 15, 3, 20, 7, 18, 9, 11]
list3 = [n for n in list2 if n > 10]
print(sum(list3))
# Задача 3:

city = ["москва", "санкт-петербург", "казань"]
city_title = [word.title() for word in city]
print(city_title)
