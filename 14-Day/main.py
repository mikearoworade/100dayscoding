from art import logo, vs
import random
from game_data import data


def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Display art
print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True

# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b

    # Making account at position B become the next account at position A.
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 15)
    print(logo)
    # Get follower count for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You are right! Current score {score}\n")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
