import random
from hangman_words import word_list
from hangman_art import stages


print(r""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/"""
      )
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}!")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"you guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"****************************IT WAS {chosen_word}! YOU LOSE.***************************")

    if "_" not in display:
        print("You win")
        game_over = True
        print("****************************YOU WIN********************************")

    print(stages[lives])
