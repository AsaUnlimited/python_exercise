import random


def election_counter():
    """function that count votes on two candidates"""
    count = random.randint(1, 2)
    if count == 1:
        return "A"
    else:
        return "B"


candidate_a = 0
candidate_b = 0

votes_in_each_region = round(10_000 / 3)

# votes in each region

for vote in range(votes_in_each_region):
    if election_counter() == "A":
        candidate_a += 1
    else:
        candidate_b += 1

# to find the percentage that candidate A wins in each region

region1 = votes_in_each_region / 100 * 87
region2 = votes_in_each_region / 100 * 65
region3 = votes_in_each_region / 100 * 17

print(region1, region2, region3)
