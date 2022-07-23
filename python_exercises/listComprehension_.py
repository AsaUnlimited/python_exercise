r = [s ** 2 for s in range(1, 11)]

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

o = [x for x in l if x % 2 == 0]
d = [x for x in l if x % 2 != 0]
dd = [x ** 2 if x % 2 == 0 else x / 2 for x in l]

s = ["lagos", "ogun", "jigawa", "imo", "kano", "osun"]
caps = [x.title() for x in s]

words = "This is so much fun programming"
vowels = "aeiou"
no_vowel = ''.join(char for char in words if char not in vowels)

listword = ["cool", "dude"]
joined_word = '...'.join(listword)

nested_lst = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(nested_lst[1][2])

# negative indexing
print(nested_lst[-1][-1])

# printing through nested list

for l in nested_lst:
    for val in l:
        print(val)

# nested list comprehension
[[print(val) for val in l] for l in nested_lst]

board = [[num for num in range(1, 4)] for num in range(1, 4)]

board2 = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for num in range(1, 4)]

board3 = [["*" for x in range(1, 4)] for x in range(1, 4)]

print(board3)

c = [x for x in zip(a, b)]

print(joined_word)

# enumerate goes through a list and also index
for x, element in enumerate(s):
    print(x, element)
