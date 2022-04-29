def rotate_list(lst: list, x: int):
    my_list = lst.copy()
    for i in range(0, len(lst)):
        my_list[x] = lst[i]
    return my_list


print(rotate_list([1, 2, 3, 4, 5], 3))


def rotate(lzt: list, y):
    y = y % len(lzt)
    return lzt[-y:] + lzt[:-y]


print(rotate([1, 2, 3, 4, 5], 3))
