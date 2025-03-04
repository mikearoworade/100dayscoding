# Project Treasure Island
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
answer = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': \n")
if answer == "left" or answer == "Left":
    answer = input("You\'ve come to a lake, Do you want to swim or wait for a boat ? "
                   "Type 'swim' or 'wait': \n").lower()
    if answer == "wait":
        answer = input("You arrive at the island unharmed. There are 3 doors"
                       "Which door will you like to go through?\n"
                       "Type red, blue or yellow: \n")
        if answer == "red":
            print("You just opened the door to hell. Game over!")
        elif answer == "blue":
            print("You just opened the door to pacific ocean. Game over!")
        elif answer == "yellow":
            print("You just opened the gate of heaven and found the treasure. "
                  "Congratulations, you win!!")
        else:
            print("Sorry, you chose a door that doesn't exist, you lost. Game over!")

    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
