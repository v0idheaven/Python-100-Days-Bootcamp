# WAY TO FIND TREASURE
print("Welcome to Treasure Island")
print("Your mission is to find treasure")
choice1 = input("You are at crossroad, where do you want to go? Type 'left' or 'right'\n").lower()
if choice1 == 'left':
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'swim' to swim across or Type 'wait' to wait for a boat.\n").lower()
    if choice2 == 'wait':
        choice3 = input("You arrived at the island. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")
        if choice3 == 'yellow':
            print("You found the treasure: You Win!")
        elif choice3 == 'red':
            print("It's a room full of fire. Game Over.")
        elif choice3 == 'blue':
            print("You enter a room full of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exists. Game Over.")
    else:
        print("You got attacked by an angry trout. Game over")
else:
    print("You felt into a hole, Game Over")