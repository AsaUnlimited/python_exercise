class MyOwnDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Modified: no zero more based index")
        return super().__getitem__(index - 1)


d = MyOwnDict()
d[1] = "Nigeria"
d[2] = "Ghana"
d[3] = "Togo"
d[4] = "Mali"
d[5] = "South Africa"

with open("my_dict_file.txt", mode='w') as my_dict:
    my_dict.write(str(d))
