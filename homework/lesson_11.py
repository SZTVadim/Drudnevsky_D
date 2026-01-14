# ЗАДАНИЕ 1: Работа с кортежами
coordinates = (10, 20, 30, 20, 10, 20, 40)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
print(30 in coordinates)
print(coordinates.index(20))
print(coordinates.count(20))
print(coordinates.count(50))
print(len(coordinates))

# ЗАДАНИЕ 2: Операции с кортежами

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]
tuple1 = tuple1 + tuple2
tuple3 = tuple1 * 3
x, y, z, *_ = tuple1
first, *middle, last = tuple(numbers)
numbers = tuple(numbers)
tuple_even = tuple(x for x in range(11))
tuple_square = tuple(x**2 for x in range(1, 6))
tuple_one = (42,)
git