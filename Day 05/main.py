fruits = ["Apple","Peach","Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)


# SUM FROM 0 TO 100
sum = 0
for i in range(0,101):
    sum += i
print(sum)    

# SUM OF ALL EVEN NUMBERS FROM 0 TO 100
sum = 0
for i in range(0,101,2):
    sum += i
print(sum)

sum2 = 0
for i in range(0,101):
    if i % 2 == 0:
        sum2 += i
print(sum2)

sum3 = 0
for i in range(0,101):
    if i%3 == 0:
        continue
    else:
        print(i)


# FIZZ BUZZ GAME
for number in range(0,101):
    if number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 ==0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)

# AVERAGE HEIGHT
student_heights = input("Input a list of student heights\n").split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for i in range(0, len(student_heights)):
    total_height += student_heights[i] 
print(f"Total height = {total_height}")  

number_of_students = 0
for i in range(0,len(student_heights)):
    number_of_students += 1
print(f"Total number of students = {number_of_students}")

print(f"Average height = {int(total_height / number_of_students)}")


# HIGHEST SCORE
student_score = input("Input a list of student score\n").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest_score = 0
for i in range(0, len(student_score)):
    if student_score[i] > highest_score:
        highest_score = student_score[i]
print(f"The highest score in the class is: {highest_score}")