try:
    num = int(input("Enter Number: "))
    for n in range(1, num + 1):
        if n % num == 0:
            print(f"{n} is factor of {num}")
except ValueError:
    print("This is a value error")
