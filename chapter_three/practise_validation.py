a = b = 7
print('a is ', a, '\nb is', b)

# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end=' ')
#     print()


for row in range(2):
    for column in range(10):
        print('@', end=' ')
    print()
