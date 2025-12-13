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