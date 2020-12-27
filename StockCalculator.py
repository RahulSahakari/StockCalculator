amount = int(input("Amount: "))
interest = int(input("Interest Rate(Percentage: "))
No_of_years = int(input("No of years: "))

def future(amount,interest,noofyears):
    count = 0
    ans = 0
    while count < noofyears:
        som = amount * interest / 100
        # 
        amount = amount + som
        gdp = amount * 0.090 / 100
        amount += gdp
        count +=1
        print(amount)

future(amount,interest,No_of_years)