import math

user_input = int(input("Enter Number: "))
user_input_length = math.ceil(math.log10(user_input))
if (user_input * user_input) % (10 ** user_input_length) == user_input:
    print(user_input, "is Ambigram")
else:
    print(user_input, "is not Ambigram")
