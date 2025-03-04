# Code to randomly pick who to pay
import random
friends = ["Alice", "Bob", "Charles", "David", "Emmanuel", "Frank"]
print(friends)

random_num_btw_friends = random.randint(0, len(friends) - 1)
print("Who is to pay for the bill? It's", friends[random_num_btw_friends])

# Using choice
print("Who is to pay for the bill? It's", random.choice(friends))
