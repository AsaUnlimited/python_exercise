# it's an unchanging way of storing ordered data
# its Immutable, cannot be changed
# tuple can have multiple data
# tuple are faster than list

# declare tuple
alphabets = ('a', 'b', 'c', 'd', 'e')
num = (1, 2, 2, 3, 4, 5, 5)
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')

# Accessing elements in a tuple
print(months[0])

# tuples can be used as keys in a dictionary but list cant
# can be used to store coordinates of a location
locations = {
    (32.345, 23.124): "Lagos Office",
    (43.21, 54.132): "Abuja Office",
    (45.431, 44.771): "Ibadan Office"
}

print(locations.items())

# finding the coordinates of an office
print(locations[(45.431, 44.771)])

# looping through a tuple
a = len(months) - 1
while a >= 0:
    print(months[a])
    a -= 1

# tuple methods
# count, # index

print(num.count(2))
print(num.count(3))
print(num.index(4))
print(num.index(2))

# nested Tuple

nested_num = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for n in nested_num:
    for m in n:
        print(m)

# set slicing
print(nested_num[1:2])
print(nested_num[1:])
