import random
import my_module

#random integer
random_int = random.randint(0, 10)
print(random_int)

#random float
random_float = random.random()
random_float *= 10
print(random_float)

print(my_module.pi)
 

# Toss a Coin
random_num = random.randint(1,2)

if random_num == 1:
    print('Heads')
else:
    print('tail')


# LIST
fruits = ["Apple", "Banana", "Grapes"]
print(fruits[0])
fruits.append("Mango")
print(fruits)
fruits.extend(["pineapple","Gauava"])
print(fruits)


# RANDOM METHOD TO PAY THE BILL
Names_string = input("Give me everybody's names, seprated by a comma. \n")
Names = Names_string.split(", ")
random = random.randint(0,len(Names)-1)
print(f"{Names[random]} is going to buy the meal today!")


# NESTED LISTS
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)


#WHERE DO YOU WANT TO PUT THE TREASURE
#we have to select 1 place in this matrix
row1 = ["🎁","🎁","🎁"]
row2 = ["🎁","🎁","🎁"]
row3 = ["🎁","🎁","🎁"]


map = [row1, row2, row3]
#PRINT ALL THE ROWS AND COLUMN
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#Mamke it in horizontal and vertical
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal - 1] = "🪙"

print(f"{row1}\n{row2}\n{row3}")
