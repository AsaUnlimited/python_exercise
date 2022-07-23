def most_frequent(Lst):
    counter = 0
    num = Lst[0]

    for i in Lst:
        curr_frequency = Lst.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


lst = [1, 2, 9, 2, 4, 2, 2]
# lzt = [i for i in lst if ]
print(most_frequent(lst))


def most_frequents(Lst):
    return max(set(Lst), key=Lst.count)


print(most_frequents(lst))
