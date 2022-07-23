def divide(a, b):
    try:
        answer = a / b
    except ZeroDivisionError as err:
        print("You cant divide by zero pls")
        print(err)
    except TypeError:
        print("a and b must integers only")
    else:
        print(f"{a} divided by {b} is {answer}")


print(divide(1, 2))
print(divide(1, 0))
print(divide(1, 'a'))
