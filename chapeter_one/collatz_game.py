user_input = int(input("Enter Number: "))
number = user_input
while number != 1:
    if number % 2 == 0:
        number = number // 2
    elif number % 2 == 1:
        number = number * 3 + 1
    print(number, end=" ")



