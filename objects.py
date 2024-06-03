# Object types
x = 10        # int object
y = 3.14      # float object
name = "Alice"  # str object
numbers = [1, 2, 3, 4, 5]  # list object
person = {"name": "Bob", "age": 30}  # dict object

# Defining and using custom objects/classes
# Defining a class

class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object/instance of a class
my_dog = Dog("Buddy", 3)
print(my_dog.description())  # Output: Buddy is 3 years old
print(my_dog.speak("Woof Woof"))  # Output: Buddy says Woof Woof

# Methods: Functions defined within a class that operate on instances of the class

class MyClass:
    class_attr = "I am a class attribute"
    # Instance method
    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    @classmethod
    def class_method(cls):
        return f"Class method: {cls.class_attr}"

    @staticmethod
    def static_method():
        return "Static method called"

#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

my_cat = Cat("Whiskers")
my_dog = Dog("Rover")

print(my_cat.speak())  # Output: Whiskers says Meow
print(my_dog.speak())  # Output: Rover says Woof

# Encapsulation:the concept of wrapping data and methods within a class and restricting access to some of the object's components.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age

my_dog = Dog("Buddy", 3)
print(my_dog.get_age())  # 3
my_dog.set_age(5)
print(my_dog.get_age())  # 5

# Polymorphism: Allows different classes to be treated as instances of the same class through a common interface.

class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.make_sound())
