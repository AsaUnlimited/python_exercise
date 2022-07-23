user_input = input("Enter a word: ")
if len(user_input) < 5:
    print(f"{user_input} is less than 5")
elif len(user_input) > 5:
    print(f"{user_input} is greater than 5")
else:
    print(f"{user_input} is equal to 5")