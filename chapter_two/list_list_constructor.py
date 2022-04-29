# Generate list from 1 to 10
import sys

print([i for i in range(1, 11)])

# for numbers between 1 - 10 multiple of 2

print([i ** 2 for i in range(1, 11)])

# for list collection of even numbers

evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)

# for even numbers collection and double of odd from 1 to 10

print([i if i % 2 == 0 else i ** 2 for i in range(1, 11)])

# to collect input and save it in a list

# print([int(input("Enter Number: ")) for i in range(1, 2)])

list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
print(list_nested_for)

upper_names = [name.upper() for name in ['dolapo', 'tolani', 'florence']]
print(upper_names)

# to create a dict from list

list_of_dict = [{key: value} for key, value in zip(upper_names, evens)]
print(list_of_dict)

# generator expression

gen = (i for i in range(1, 11))
# list comprehension
lst = [i for i in range(1, 11)]

dict_comp = {k: v for k, v in zip(range(5), range(5))}
print(dict_comp)


# print(sys.getsizeof(gen))
# print(sys.getsizeof(lst))

def get_first(s: str) -> str:
    return s[0]


l = [get_first(val) for val in ['Hello', 'How', 'Are', 'You']]
print(l)
