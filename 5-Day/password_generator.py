# Password Generator
import random

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to Password Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

all_characters = []

for i in range(nr_letters):
    all_characters.append(letters[random.randint(0, len(letters)-1)])
for j in range(nr_symbols):
    all_characters.append(symbols[random.randint(0, len(symbols)-1)])
for k in range(nr_numbers):
    all_characters.append(numbers[random.randint(0, len(numbers)-1)])
print(all_characters)
random.shuffle(all_characters)
print(all_characters)
password = "".join(all_characters)
print(f"Your password is: {password}")
