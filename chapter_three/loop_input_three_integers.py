x = 1
num = []
while x <= 4:
    numz = int(input('Enter inters to get the sum, product and average: \n'))
    num.append(numz)
    x += 1
ans_sum = 0
for y in num:
    ans_sum += y
print(f' the sum of the integers are {ans_sum}\n')
ans_product = 1
for z in num:
    ans_product *= z
print(f'the product of the integers are {ans_product}\n')
ans_average = ans_sum / len(num)
print(f' the average of the integers are {ans_average}\n')