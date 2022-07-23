import random


def dice_roll():
    """:return between 1 and 6 when dice is rolled"""
    dice = random.randint(1, 6)
    if dice == 1:
        return "count_one"
    elif dice == 2:
        return "count_two"
    elif dice == 3:
        return "count_three"
    elif dice == 4:
        return "count_four"
    elif dice == 5:
        return "count_five"
    else:
        return "count_six"


count_one = 0
count_two = 0
count_three = 0
count_four = 0
count_five = 0
count_six = 0
for each_roll in range(10_000):
    if dice_roll() == "count_one":
        count_one += 1
    elif dice_roll() == "count_two":
        count_two += 1
    elif dice_roll() == "count_three":
        count_three += 1
    elif dice_roll() == "count_four":
        count_four += 1
    elif dice_roll() == "count_five":
        count_five += 1
    else:
        count_six += 1

total_ratio = count_one + count_two + count_three + count_four + count_five + count_six
ratio = total_ratio / 6

print(ratio)
