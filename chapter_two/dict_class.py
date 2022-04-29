my_dict = {
    'name': "segun",
    'age': 12,
    'sex': 'male',
    'hobby': ['Python', 'Java'],
    "is_wife_beater": False
}

print(len(my_dict))

for key in my_dict:
    print(key)
    print(key, '---', my_dict[key])

# will give keys
for key in my_dict.keys():
    print(key)
    print(key, '---', my_dict[key])

# will give values
for value in my_dict.values():
    print(value)
    print(value, '---', my_dict[key])

# print the items
for key, value in my_dict.items():
    print(key, '---', value)

# print items grouped together
print(my_dict.items())
