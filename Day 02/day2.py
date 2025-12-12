num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)
print("Your name has " + new_num_char +  " characters.")


user_input = input("Type a two digit number: ")
first_digit = int(user_input[0])
second_digit = int(user_input[1])

print(first_digit + second_digit)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height**2)

print("Your BMI is: ",round(bmi,2))