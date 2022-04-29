facto = 1
num = int(input('Enter number to calculate its factorial: '))
if num == 0 or num == 1:
    print(f'{num}')
else:
    for i in range(1, num + 1):
        facto = facto * i
    print(facto)

import math


def fact(numz):
    return math.factorial(numz)


print(fact(7))
