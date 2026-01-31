"""ЧАСТЬ 1: Абстракция - Абстрактный класс Animal"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


"""ЧАСТЬ 2: Наследование - Классы Dog и Cat"""


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-Гав! ")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


"""ЧАСТЬ 3: Инкапсуляция - Класс Zoo (Зоопарк)"""


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animals(self, animal):
        self.__animals.append(animal)

    def get_animals(self):
        return self.__animals

    def get_animals_count(self):
        return len(self.__animals)

    def animal_sound(self, animal):
        animal.make_sound()  # Потомучто у нас есть этот метод другом классе и мы его вызываем по своему


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")
zoo.add_animals(cat1)
zoo.add_animals(dog1)
zoo.add_animals(dog2)

print(zoo.get_animals())

for animal in zoo.get_animals():
    zoo.animal_sound(animal)


# object1 = Animal()
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
#  не дает создать экземпляр абстрактного класса, т.к по сути это шаблон, а не конкретный класс")
