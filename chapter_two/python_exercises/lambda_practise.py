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


