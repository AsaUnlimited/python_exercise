user_input = int(input("Enter number: "))
factor = 1
sum_of_factors = 0
while factor < user_input:
    if user_input % factor == 0:
        sum_of_factors += factor
    factor += 1
if sum_of_factors > user_input:
    print(user_input, "is abundant number")
elif sum_of_factors == user_input:
    print(user_input, "is perfect Number")
else:
    print(user_input, "is a deficient Number")
