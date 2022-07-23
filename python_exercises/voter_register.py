

# vote register using dictionary

voted = {}


def voter_check(name):
    if voted.get(name):
        return f'you have voted already'
    else:
        voted["name"] = True
        return f'please step forward to cast your vote'


def plusMinus(arr):  # Write your code here
    negative_count = 0
    zero_count = 0
    positive_count = 0
    for i in arr:
        if i == 0:
            zero_count += 1
        elif i < 0:
            negative_count += 1
        else:
            positive_count += 1

    zero_percent = zero_count / len(arr)
    negative_percent = negative_count / len(arr)
    positive_percent = positive_count / len(arr)

    print(f"{positive_percent:.6f}")
    print(f"{negative_percent:.6f}")
    print(f"{zero_percent:.6f}")


def minMaxSum(arr):
    maxTotal = max(arr)
    minTotal = min(arr)
    maxSum = sum(arr) - maxTotal
    minSum = sum(arr) - minTotal
    ans = minSum, maxSum
    return ' '.join(map(str, ans))


lzt = [1, 2, 3, 4, 5]
# print(voter_check(name))
lst = [1, 1, 0, -1, -1]
# print(plusMinus(lst))
print(minMaxSum(lzt))
