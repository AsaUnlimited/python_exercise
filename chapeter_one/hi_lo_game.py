user_input = int(input("Enter a Number Between 10 - 50: "))
number = 10
while user_input < number:
    print("Too Low")
    continue
while user_input > number:
    print("Too High")
