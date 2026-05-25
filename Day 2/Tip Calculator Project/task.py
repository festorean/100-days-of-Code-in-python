print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
totalTip = 1.00 + (tip / 100)
pay = (bill / people) * totalTip
print(f"Each person should pay: ${pay:.2f}")


