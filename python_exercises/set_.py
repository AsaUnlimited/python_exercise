# set are collection of unordered data items with no duplicate values
# set is faster than dictionary and list
# set are like formal mathematical set
# set elements can't be accessed by their index


# to declare set
s = {1, 2, 3}

# using set function
s2 = set({1, 2, 3})

s3 = {1, 2, 'a', 23.5, 'b', 4}
print(s3)

# confirm an elements is present in a set
ch = 1 in s3
print(ch)

# loop through a set
for c in s3:
    print(c)

# set can be used to summarize in imformation
cities = {"lagos", "imo", "Kaduna", "kano", "Oyo", "Jigawa", "lagos", "imo", "Kaduna", "Kaduna", "kano", "Oyo",
          "Jigawa", "lagos", "lagos"}
print(list(cities))

# set methods
# add
s3.add(7)
print(s3)

# remove, remove throws error if the item is not in the list
# discard, does not throw error if the item is in the list

s3.remove(7)
print(s3)

# copy

s4 = s3.copy()
print(s4)

# clear

s3.clear()
print(s3)

# set union |
java_student = {"segun", "shamson", "Funmi", "Tolani", "wale", "Jonathan", "florence"}
python_student = {"zeepy", "sandra", "advanceWorm", "Jonathan", "wale"}

students = java_student | python_student
print(students)

# set intersection
students = java_student & python_student
print(students)

# set comprehension
setX = {x ** 2 for x in range(1, 11)}
print(setX)

# ca be used to generate is dictionary
setD = {x: x ** 2 for x in range(1, 11)}
print(setD)


def vowelcheck(str):
    return len({char for char in str if char in 'aeiou'}) == 5


print(vowelcheck('sequoia'))
