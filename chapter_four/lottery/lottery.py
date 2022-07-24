import random

lottery_guess = eval(input("Enter Your lucky number: "))
lottery = random.randint(1, 100)
lottery_first_num = lottery // 10
lottery_second_num = lottery % 10
lottery_guess_first_num = lottery_guess // 10
lottery_guess_second_num = lottery_guess % 10
if lottery_guess == lottery:
    print(f"you are a star, You win $10,000")
elif lottery_first_num == lottery_guess_second_num and lottery_guess_first_num == lottery_second_num:
    print("You rock, you win $300")
else:
    print(f"The lucky Number is: {lottery}")
    print("Try again!!!")


print(lottery)