import math


# using while loop
def facto(x):
    p = 1
    c = 1
    while c < x:
        p *= c
        c += 1
    return p


result = facto(10)
print(result)

# using inbuilt factorial function
print(math.factorial(10))


# using recursion
def r_facto(n):
    if n == 1:
        return 1
    else:
        return n * r_facto(n - 1)


ans = r_facto(10)
print(ans)
