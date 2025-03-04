# Tip Calculator
print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))

each_pay = (total_bill + (total_bill * tip / 100)) / num_people
print(f"Each person should pay: ${each_pay:.2f}")



