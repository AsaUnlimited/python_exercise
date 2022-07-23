# we create class

# __init__ (dunda method) is used to initialize variable.

class Player:

    def __init__(self, nameless: str, age: int) -> None:
        self.name = nameless
        self.age = age


# create object of a class
player1 = Player("Messi", 33)
player2 = Player("Kanu", 45)

print(player1.name)
print(player1.age)
print(player2.name)

# class MyClass:
#     def shout(self):
#         print("Yaay")


# my_class = MyClass()
# my_class.shout()


