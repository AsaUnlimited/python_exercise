print('Enter two integers and i will tell you their relationships')

num1 = int(input('Enter first integer: '))
num2 = int(input('Enter second integer: '))

if num1 == num2:
    print(f'{num1} is equal to {num2}')
if num1 != num2:
    print(f'{num1} is not equal to {num2}')
if num1 < num2 and num1 <= num2:
    print(f'{num1} is less than or equal to {num2}')
if num1 > num2 and num1 >= num2:
    print(f'{num1} is greater than or equal to {num2}')

