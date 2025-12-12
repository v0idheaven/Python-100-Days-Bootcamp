print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? \n₹ "))
tip = int(input("What percentage tip would you like to give?\n"))
total_person = int(input("How many people to split the bill?\n"))

pay1 = total_bill + (total_bill * tip / 100)

pay2 = pay1 / total_person
print(f'Each person should pay: ₹{round(pay2, 2)}')