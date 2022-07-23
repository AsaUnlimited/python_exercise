class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("Index Out Of Bound")
        return super().__getitem__(index - 1)

    def __setitem__(self, key, value):
        pass


l = CustomList()
l.append(1)
l.append(5)
print(l)
