import math

user_input = int(input("Enter number: "))
input_sqrt = math.sqrt(user_input)
input_ceil = math.ceil(input_sqrt)
if input_ceil % 2 != 0:
    print(user_input, "is a prime number")
else:
    print(user_input, "is not a prime number")
