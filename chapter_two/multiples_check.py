num = int(input('Enter Number: '))
multiples = int(input('Enter Multiple: '))
ans = 1
while ans < multiples:
    ans *= num
    if ans == multiples:
        print(f'{num} is a multiple of {multiples}')
        break
    else:
        print(f'{num} is not a multiples of {multiples}')

# arr = input("Enter space separated numbers: ").split(" ")
# lst = list(map(int, arr))
# print(arr)
# print(lst)
# for i in arr:
#     print(int(i) * 2)
# print()
