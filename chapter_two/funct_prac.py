from typing import Tuple


def add(a: int = 2, b: str = 'color') -> Tuple[int, str]:
    return a, b


print(add(3, "3"))
print(add(3))
print(add())
print(add(b="you", a=5))


# add()__doc__
# * args will pack all input together to be able to work on it

def add_up_parameter(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(add_up_parameter(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
# can be used to unpack also
print(add_up_parameter(*[1, 2, 3, 4, 5, 6]))
# is used to unpack when passing a list as an argument
lst = [12, 22, 34, 54, 25]
print(add_up_parameter(*lst))


# **kwargs will pack all and return dictionary
def dict_pack_unpack(**kwargs):
    print(kwargs)


dict_pack_unpack(name="shola", age=45, sex="male", complexion="brown-skin")


def dict_pack_unpack(*args, **kwargs):
    print("kwargs", kwargs)
    print("Args", args)


dict_pack_unpack(23, 12, "Asa", name="amaka", age=45, sex="female", complexion="brown-skin")


def add(a, b):
    """adds two number together"""  # doc reference.
    return a + b

print(add.__doc__name)
