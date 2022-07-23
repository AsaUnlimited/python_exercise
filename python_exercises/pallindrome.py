import math


def pallindrome(word):
    return word == word[::-1]


print(pallindrome("12321"))
