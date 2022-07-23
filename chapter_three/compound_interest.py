amount = int(input("Enter amount invested: "))
no_of_years = int(input("Enter number of years: "))
rate = int(input("Enter interest amount: "))

interest_rate = amount / 100 * rate

for year in range(no_of_years):
    amount_ = amount * (1 + interest_rate) ** year
    print(amount_)
