#  String iteration, {start ; stop : step}

# using list constructor
# join them together declaring it this way
lst = list("abcdefghijk")
print(lst)

# using square bracket, each element is put in ''
lsd = ['0', 'b', '1', 'd', '3']
print(lsd)

print("".join(lsd))

# slicing
print((lst[1:5]))

# reverse
print(lst[::-1])

# multiply list by 2.
print(lst * 2)

# using plus operator [+] to join two list together will not change the list.
lst + [1, 2, 3, 4]
print(lst)

# using augmented assignment
lst += [1, 2, 3, 4]
print(lst)

# check membership
print('a' in lst)
print('q' in lst)
print('q' not in lst)

# add another data to a list
lst.append(7)
print(lst)

lsd.append([6,8,9])
print(lsd)

lsd.extend([6,8,9])
print(lsd)

fruits = ['banana', 'orange', 'apple', 'guava']
fruits.extend("pineapple")
print(fruits)
