# decorator,
class Playground:
    count = 0

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Playground.count += 1

    def repr(self):
        return f"<Playground: {self._name}>"

    def str(self):
        return f"Playground{{name={self._name}, age={self._age}}}"

    # def del(self):
    #     Playground.count -= 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def function_only():
        return "Am on my own"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age


p1 = Playground("Omosetan", 25)
p2 = Playground("Omorele", 2)
print(Playground.count)
print(p1.count)
p1.count = 3
print(p1.count)

print(Playground.count)
del p1
print(Playground.count)