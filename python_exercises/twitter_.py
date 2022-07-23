twitter_users = [
    {'username': '@sikade', 'age': 29, 'email': 'sikade2007@gmail.com', 'phone': '08086992338', 'verified': True,
     'tweets': ['i am king', 'i rule my world', 'i am a proud african']},
    {'username': '@Asa', 'age': 31, 'email': 'asa001@gmail.com', 'phone': '09130386857', 'verified': True,
     'tweets': ['thankful', 'i am a winner', 'i am a nigerian', 'we dont take shit']},
    {'username': '@amaka', 'age': 20, 'email': 'amaka2000@yahoo.com', 'phone': '08033792338', 'verified': True,
     'tweets': ['i serve a living God', 'heaven is real']},
    {'username': '@asaflo', 'age': 23, 'email': 'asaflo007@gmail.com', 'phone': '08022292338', 'verified': False,
     'tweets': ['the queens', 'i love jesus', 'heaven is real', 'repent, heaven is real',
                'give your life to christ']},
    {'username': '@sandra', 'age': 22, 'email': 'sandra2002@gmail.com', 'phone': '08077992338', 'verified': False,
     'tweets': ['little birds', 'we aspire to...', 'feel free to lick your screen', 'we here to stay',
                'tech lady']},
    {'username': '@easycare', 'age': 19, 'email': 'easycare2010@gmail.com', 'phone': '08145992338', 'verified': True,
     'tweets': ['i love python', 'tech youngster', 'i wanna buy range rover', 'tech leads']},
    {'username': '@ordinaka', 'age': 27, 'email': 'ordinaka@gmail.com', 'phone': '0803333344555', 'verified': False,
     'tweets': ['kingcoder', 'we run the world', 'tech lord', 'vacations', 'love and money']},
    {'username': '@tobymyg', 'age': 17, 'email': 'tobymyg@gmail.com', 'phone': '098086992338', 'verified': True,
     'tweets': ['i am king', 'rule your world']},
    {'username': '@yemisi', 'age': 21, 'email': 'yemisi76@gmail.com', 'phone': '08086992338', 'verified': True,
     'tweets': []},
    {'username': '@sisilove', 'age': 24, 'email': 'sisiloveofgog@gmail.com', 'phone': '0905790754234',
     'verified': False,
     'tweets': ['jesus my rock', 'believe in God', 'let love lead', 'we are made in God image',
                'we will  overcome', 'love conquers it all']}
]

# verified_user = []
# for v in twitter_users:
#     if v["verified"]:
#         verified_user.append(v)
# print(verified_user)

verified_user_comp = [v["username"] for v in twitter_users if v["verified"] is True]
print(verified_user_comp)
# using list comprehension
user_ages = [ages["age"] for ages in twitter_users]

# using map
map_user = map(lambda y: y['username'], filter(lambda x: x['verified'], twitter_users))

map_user2 = filter(lambda x: x, map(lambda x: x['username'] if x['verified'] else False, twitter_users))
user_age_max = max(user_ages)
print(user_age_max)

user_age_min = min(user_ages)
print(user_age_min)

user_average_age = sum(user_ages) / len(user_ages)
print(user_average_age)

active_users = [a["username"] for a in twitter_users if a["tweets"] != []]
print(active_users)

user_below_25_active = [user['username'] for user in twitter_users if user['age'] < 25 and user['verified']]
print(user_below_25_active)

from statistics import mean

print(mean(user['age'] for user in twitter_users))

# to display the user full info from the list
most_tweets = max(twitter_users, key=lambda user: len(user['tweets']))

# to sort and display only tweets
most_tweets2 = max(twitter_users, key=lambda user: len(user['tweets']))['username']
print(most_tweets)
# ascending order
ascend = sorted(twitter_users, key=lambda user: user['age'])

# descending order
descend = sorted(twitter_users, key=lambda user: user['age'], reverse=True)

# ZIP Builtin function example
student_1 = [45, 67, 98, 78]
student_2 = [56, 87, 52]
print(list(zip(student_1, student_2)))

# you can make it strict
print(list(zip(student_1, student_2)))

my_slice = slice(1, 4, 2)
print("ayinlade"[my_slice])

# verified_user_map = map(lambda x: x == True)
# print(verified_user_map)

# lst_map = map(lambda x: x ** 2 if x % 2 == 0 else x, range(1, 10))
# print(lst_map)

# verified = [v.append() for v in twitter_users if "verified" == "True"]
# print(verified)

# print([twitter_user["verified"] == "True" for twitter_user in twitter_users])
