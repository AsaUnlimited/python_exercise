# u can build a list in declaration in list comprehension
# lst = [i for i in range(1, 10)]
# print(lst)

# to collect input and save in a list using list comprehension
# Underscore _ is used to indentify variable that is not used or needed.

# lst_input = [int(input('Enter number: ')) for _ in range(10)]
# print(lst_input)

# [j := int(input('Enter number: ')) for _ in range(10)]
# print(j)


# lsst = []
# for i in range(1, 10):
#     if i % 2 != 0:
#         lsst.append(i)
# print(lsst)

# will be written in list comprehension as
# it goes from left to right.
# lst1 = [i for i in range(1, 10) if i % 2 != 0]
# print(lst1)

# list_comp = [char(i) for i in range(65, 91)]
# print(list_comp)

# lst = []
# for i in range(65, 91):
#     lst.append(chr(i))
# print(lst)
from functools import reduce

lsst = [chr(i) for i in range(65, 91)]
print(lsst)

names = ['Amaka', 'Segun', 'comb', 'Samson', 'foil']

print(all(name.istitle() for name in names))

peoples = [{"name": "Omosetan Omorele", "age": 30, "year_of_exp": 4, "language": ["Javascript", "Python"]},
           {"name": "Omosetan Omorele", "age": 25, "year_of_exp": 2, "language": ["Python", "Java"]},
           {"name": "John Doe", "age": 32, "year_of_exp": 3, "language": ["C#", "Python"]},
           {"name": "Amaka Segun", "age": 20, "year_of_exp": 5, "language": ["Javascript", "Kotlin"]},
           {"name": "Florence Segun", "age": 30, "year_of_exp": 4, "language": ["Kotlin", "Python"]},
           {"name": "Ernest Adeola", "age": 30, "year_of_exp": 4, "language": ["Java", "Python"]}
           ]

print([people["age"] <= 28 and "Python" in people["language"] for people in peoples])

print(any([people["age"] <= 28 and "Python" in people["language"] for people in peoples]))

print([people["name"] for people in peoples if people["age"] <= 30 and "Python" in peoples])

lst_map = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
print(lst_map)

lst1 = list(lst_map)
lst2 = list(lst_map)

print("1", lst1)
print("2", lst2)


# filter function
def isEven(x):
    return x % 2 == 0


filter_obj = list(filter(isEven, range(1, 10)))
print(filter_obj)

# reduce.* function
# reduce(lambda x, y: x + y, range(1, 11))

fruits = ['Apple', 'Pear', 'Pineapple', 'Orange', 'Watermelon', 'Banana', 'Cucumber']
longest = reduce(lambda x, y: x if len(x) > len(y) else y, fruits)
print(longest)

# find a length using max method

print(max(fruits))

# using the key length

print(max(fruits, key=len))

# sorted to reverse

print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))

print(sorted(fruits, key=len, reverse=True))

# arrange to last char in the string
print(sorted(fruits, key=lambda x: x[-1]))

