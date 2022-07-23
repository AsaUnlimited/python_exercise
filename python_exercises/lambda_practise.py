# lamda example

# normal function
def add(x, y):
    return x + y


# lambda function (an anonynous function)

add = lambda x, y: x + y
sub = lambda x, y: x - y

print(add.__name__)
print(sub.__name__)


# calling a function in another function. function higher order.
# operate function is the higher order here

def add(a, b):
    return a + b


def sub(c, d):
    return d - c


# def mult(p, q):
#     return p * q


def operate(x, y, func):
    return func(x, y)


val_sub = operate(5, 24, sub)
val_add = operate(5, 24, add)
val_mult = operate(5, 24, lambda x, y: x * y)
div = operate(5, 24, lambda x, y: y / x)

print(val_add)
print(val_sub)
print(val_mult)
print(div)


def multiple(x, fx):
    return fx(x)


double = multiple(3, lambda x: x * x)
print(double)

triple = multiple(3, lambda x: x * x * x)
print(triple)

# from datetime import date
# from dataclasses import dataclass
#
#
# @dataclass
# class Registration:
#     registration_type: str
#     registration_description: str
#     registration_number: str
#     registration_student_id: int
#     registration_name: str
#
#     registration_id: int = 0
#
# def add_registration(self): return f"Application of {self.registration_name}, {self.registration_number},
# {self.registration_student_id}, {self.registration_type} \ and {self.registration_description} was successful"
#
#
# Reg1 = Registration("high schhol", "people's no.1 in yaba", "1200", "funmi", 29890)
# print(Reg1.add_registration())
#


