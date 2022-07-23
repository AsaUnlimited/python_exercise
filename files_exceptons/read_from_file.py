import json

# file_obj = open("file.txt", mode='r')

# file_obj = open("file.txt", mode='r')
# for line in file_obj.readlines():
#     for word in line.split(" "):
#         print(word)


# with open("file.txt", mode='r') as file_obj:
#     for line in file_obj.readlines():
#         for word in line.split(" "):
#             print(word)

# file_obj.close()

config_dict = {
    "name": "Adeola",
    "age": 18,
    1: "Birthday",
    "hobby": [1, 2, 3, 4],
    "bool": True
}

# with open("config_json", mode='r') as file_obj:
#     # json.dump(config_dict, file_obj, indent=4, separators=(',', ':'))
#     con = json.load(file_obj)
#     print(con)

with open("config_json", mode='r') as file_obj:
    json.dump(config_dict, file_obj, indent=4, separators=(',', ':'))
    con = json.load(file_obj)
    print(con)
