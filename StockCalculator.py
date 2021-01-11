amount = int(input("Amount: "))
interest = int(input("Interest Rate(Percentage): "))
No_of_years = int(input("No of years: "))


def future(amount, interest, noofyears):
    count = 0
    ans = 0
    while count < noofyears:
        # Som is every year the amount of of money added or rather interest
        som = (amount * interest) / 100
        # Here im adding interest to the amount
        amount += som
        # GDP or rather growth rate or something
        GDP = amount * 0.492 / 100
        amount += GDP

        count += 1
        print(f"Year No:{count}:{amount}")


future(amount, interest, No_of_years)
