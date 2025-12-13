#CHECK YOU RIDE ROLLERCOASTER OR NOT
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? \n"))
# if height >= 120:
#     print("You can ride the rolarcoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# CHECK NUMBER IS ODD OR EVEN
# number = int(input("Enter a number\n"))
# if number % 2 == 0:
#     print("This is a even number.")
# else:
#     print("This is a odd number.")


#CHECK YOU RIDE ROLLERCOASTER OR NOT IF RIDE THEN AT WHAT COAST
# print("Welcoome to rollercoaster!")
# height = int(input("What is your height in cm?\n"))
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# BMI CALCULATOR WITH DETAILS
# height = float(input("enter your height in m: \n"))
# weight = float(input("Enter your wiight in kg: \n"))

# BMI = round(weight / (height ** 2))
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are Underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you are Normal Weight")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are Over Weight")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are Obese")
# else:
#     print(f"Your BMI is {BMI}, you are Clinically obese")


# CHECKING FOR LEAP AND NOT A LEAP YEAR
# year = int(input("Which year do you want to check?\n"))

# if year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is a leap year")
# elif year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a Leap year")


# ROLLERCOASTER BILL WITH AGE AND PHOTO TAKEN
# print("Welcome to the rolarcoaster ride")
# height = float(input("What is your age in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the Rollercoaster!")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5")
#     elif age < 18:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#     photo = input("Do you want a photo? (y/n)\n")
#     if photo == "y":
#         bill += 3
#         print("Photo adds $3 to your bill.")
    
#     print(f"Your final bill is: ${bill}")

# else:
#     print("you can't ride")


# PIZZA ORDER
# print("Welcome to Pyhton pizza Deliveries")
# size = input("What size pizza do you want? S, M or L\n")
# add_pepperoni = input("Do you want pepperoni? y or n\n")
# extra_cheese = input("Do you want extra cheese? y or n\n")

# bill = 0
# if size == "S":
#     bill = 15
#     print("You Selected Small pizza")
#     if add_pepperoni == "y":
#         bill += 2
#     if extra_cheese == "y":
#         bill += 1
# elif size == "M":
#     bill = 20
#     print("You Selected Medium pizza")
#     if add_pepperoni == "y":
#         bill += 3
#     if extra_cheese == "y":
#         bill += 1
# elif size == "L":
#     bill = 25
#     print("You Selected Large pizza")
#     if add_pepperoni == "y":
#         bill += 3
#     if extra_cheese == "y":
#         bill += 1
    
#     print(f"Your final bill is: ${bill}.")

# else:
#     print("Enter Correct Size")


# #LOVE CALCULATOR
# print("Welcome to the Love Calculator")
# name1 = input("What is your name?\n")
# name2 = input("What is their name?\n")

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))
# if 90 < love_score < 10:
#     print(f"Your score is {love_score}, you go together like coke and mentos")
# elif 40 < love_score < 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}")