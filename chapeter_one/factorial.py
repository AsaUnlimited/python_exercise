user_input = int(input("Enter Number: "))
num = user_input

# factorial using if statement

factorial = 1
if num < 0:
    print("No factorial for negative numbers")
elif num == 1:
    print("factorial of 1 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)

# factorial using for loop.

ans = 1
for i in range(1, num + 1):
    ans *= i
    print(ans)

# factorial using while

counter = 1
product = 1
while counter <= num:
    product *= num
    num -= 1
    print(product)