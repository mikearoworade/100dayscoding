from random import randint
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty level: Type 'easy' or 'hard' ")
    print()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    # Choose a random number between 1 and 100.
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality
    guess = 0
    while guess != answer:
        # Track the number of turns and reduce by 1 if they get it wrong
        print(f"You have {turns} attempts remaining to guess the correct answer.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        turns =  check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess again!")

game()

