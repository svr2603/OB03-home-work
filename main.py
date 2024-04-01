#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def fly(self):
        print(f"{self.name} летает")
    def make_sound(self):
        print(f"{self.name} щебечет")

class Mammal(Animal):
    def __init__(self, name, age, predator):
        super().__init__(name, age)
        self.predator = predator

    def hunting(self):
        print(f"{self.name} охотится")
    def make_sound(self):
        print(f"{self.name} рычит")
class Reptile(Animal):
    def __init__(self, name, age, venomous):
        super().__init__(name, age)
        self.venomous = venomous

    def crawling(self):
        print(f"{self.name} ползает")

    def make_sound(self):
        print(f'{self.name} шипит')

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zookeeper():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def feed_animal(self):
        print(f"{self.name} кормит животных")

class Veterinarian():
    def __init__(self, name, age, specialization):
        self.name = name
        self.age = age
        self.specialization = specialization
    def heal_animal(self):
        print(f"{self.name} лечит животных")
class Zoo():
    def __init__(self):
        self.animals = []
        self.stuff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_stuff(self, stuff):
        self.stuff.append(stuff)
