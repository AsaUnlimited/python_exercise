# global scope
num = 1


def func1():
    # Q local scope
    num2 = 2

    def func2():
        num3 = 3


print(num)


def function(param):
    print(("Before reassignment -> ", id(param)))
    param = 5
    print("After reassignment -> ", id(param))


num = 45
print("num -> ", num)
# reassignment
num = function(num)
print("num -> ", num)
