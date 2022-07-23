# try and except catching

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator can not be zero")
# catching a type error
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        TypeError("invalid input, use your sense")

    return a / b


# print(divide(15, 3))
# print(divide(3, -1))
# print(divide(2, 0))

# using except to give exceptional values or situation
try:
    print(divide(2, 0))
except:
    print("wrong value")

num = int(input("Enter numerator: "))
den = int(input("Enter denumerator: "))

while True:
    try:
        print(print(divide(num, den)))
        break
    except:
        print("wrong value")
        num = int(input("Enter numerator: "))
        den = int(input("Enter denumerator: "))

# try with fnally

try:
    print("life is good")
    print("1 / 0")
    print("AFter Life")

except ZeroDivisionError as e:
    print("ZeroError", e)
except IndexError as e:
    print(IndexError, e)
else:
    print("Else i run only when there is no error")
finally:
    print("i run everytime")