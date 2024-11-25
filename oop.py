class Person:
    def __init__(self):
        self._age = None # 0 it coul be i don't know shoudl i even write the pole age or not but ok

    def get_age(self,):
        return self._age

    def set_age(self, age):
        if age < 0:
            print("age cannot be negative")
        else:
            self._age = age


p = Person()
p.set_age(25)
print(p.get_age())
p.set_age(-5)

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "Meow"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())
print(cat.name, cat.speak())

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Car is driving"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"

def move(vehicle):
    return vehicle.move()

car = Car()
bike = Bicycle()

print(move(car))
print(move(bike))

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius **2 * 3.1415


rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())
print(circle.area())