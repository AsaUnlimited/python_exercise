# while True:
#     try:
#         user_input = int(input("Enter a number"))
#         print(user_input)
#         break
#     except ValueError:
#         print("Try again")

# while True:
#     try:
#         input_str = input("Enter a word: ")
#         input_num = int(input("Enter an index: "))
#         break
#     except ValueError:
#         print("Enter a valid number")
#     except IndexError:
#         print("Index out of bound")

user_input = input("Enter you name: ")
last_letter = user_input[-1]
print(last_letter)