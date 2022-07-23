import collections


def custom_for(iterable, func):
    it = iter(iterable)

    while True:
        try:
            func(next(it))
        except StopIteration:
            break


def cube(num):
    print(num ** 3)


print(custom_for([1, 2, 3, 4, 5], cube))


# Generator
def gen():
    count = 0
    while True:
        yield count
        count += 1


# infinity generation loop
# for i in gen():
#     print(i)


# generator that behaves like range.
def counter(low, high, step):
    while low < high:
        yield low
        low += step


for i in counter(2, 20, 2):
    print(i)


# creating a class using collections
Person = collections.namedtuple("Person", "name age")

p1 = Person(name="Asa", age=16)

print(p1.name)

print("""
********************************
        TIC TAC TOE
********************************

""")

