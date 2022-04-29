num = int(input('Enter number to check if its palindrome: '))
num1 = num // 10000
num2 = num % 10000
num2 //= 1000
num3 = num % 1000
num3 //= 100
num4 = num % 100
num4 //= 10
num5 = num % 10
if num1 == num5 and num4 == num2:
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')