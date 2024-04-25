way_of_invest = input("Lumpsum or SIP: ").lower()
if way_of_invest == "lumpsum":
    amount = float(input("Amount: "))
    interest_rate = float(input("Interest Rate (p/a): "))
    interest_rate /= 100
    time = int(input("Time Period in years: "))
    FV = amount*((1+interest_rate)**time)  # FV means the future value
    FV = round(FV, 2)  # rounding to 2 decimal places
    print(f"Your money after {time} years: {FV}")
elif way_of_invest == "sip":
    amount = float(input("SIP amount(monthly): "))
    amount *= 12
    interest_rate = float(input("Interest Rate (p/a): "))
    interest_rate /= 100
    time = int(input("Time Period in years: "))
    FV = 0
    for i in range(0, time):
        gap = time - i
        value = amount*((1+interest_rate)**gap)
        FV += value
    FV = round(FV, 2)
    print(f"Your money after {time} years: {FV}")
else:
    print("Wrong choice")
