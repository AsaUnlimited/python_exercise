class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "I speak"

    def eat(self):
        return "I eat"


class Dog(Animal):
    def __init__(self, name, type_, age):
        super().__init__(name, age)
        self.type = type_

    def speak(self):
        return "Dog speak"


class Cat(Animal):
    pass


dog = Dog("jack", "Local")

print(dog.name, dog.type)
