user_input = int(input("Enter Number: "))
num1, num2 = 0, 1
if user_input == 1:
    print(num2)
else:
    print(num1)
    for i in range(user_input - 1):
        ans = num1 + num2
        num1 = num2
        num2 = ans
        print(ans)