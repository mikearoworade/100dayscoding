import random
print("Welcome to Rock Paper Scissors!\n")
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
symbol = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer_choice = random.randint(0, 2)
if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(symbol[player_choice])
    print(f"Computer chose: {computer_choice}")
    print(symbol[computer_choice])

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 0 and computer_choice == 1:
        print("You lose!")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice == 1 and computer_choice == 0:
        print("You win!")
    elif player_choice == 1 and computer_choice == 2:
        print("You lose!")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif player_choice == 2 and computer_choice == 1:
        print("You win!")
