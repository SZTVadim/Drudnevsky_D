# ЗАДАНИЕ 1:

fruits = {"яблоко", "банан"}
fruits.add("апельсин")
fruits.update({"груша", "виноград "})
fruits.discard("банан")
# fruits.discard("киви") игнорирует
# fruits.remove("киви")  вызывает ошибку
random_fruit = fruits.pop()
print(random_fruit)
print(fruits)

# ЗАДАНИЕ 2*:
group1 = {"Иван", "Мария", "Петр", "Анна"}
group2 = {"Петр", "Анна", "Сергей", "Ольга"}
# для поиска пересечений, воспользуюсь
# {первое_множестов}.intersection(второе_множестов, третье_множество)
inters = group1.intersection(group2)
print(inters)
# Для объединения воспользуюсь методом  .union()
# x = set1.union(set2), так же можно использовать set1 | set2
union_set = group1.union(group2)
print(union_set)
# Для поиска расности исп:  .difference()
# set = set1.difference(set2) из первого set удалит значения второго set
deff_set = group1.difference(group2)
print(deff_set)
