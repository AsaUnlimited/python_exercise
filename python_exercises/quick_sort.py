def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return sorted(less) + [pivot] + sorted(greater)


def printlst(arr):
    for l in arr:
        print(l)


def double_val(arr):
    res = [i ** 2 for i in arr]
    return res


def double_val_first(arr):
    f = arr[0] ** 2
    arr[0] = f
    return arr


def multiply_array(arr):
    for i in arr:
        for j in arr[i]:
            return arr[i] * arr[j]


def appendAndDelete(s, t, k):
    # Write your code here
    match_char = 0
    for (charS, charT) in zip(s, t):
        if charS == charT:
            match_char += 1
        else:
            break
    total_length = len(s) + len(t)
    if (2 * match_char + k >= total_length and total_length % 2 == k % 2) or total_length < k:
        return "Yes"
    return "No"


# lst = [10, 8, 4, 11, 15]
# print(quick_sort(lst))
# print(printlst(lst))
# print(double_val(lst))
# print(double_val_first(lst))
# print(multiply_array(lst))
