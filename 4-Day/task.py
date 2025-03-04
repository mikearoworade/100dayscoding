# Random module
import my_module
import random

# What is a module: responsible for different functionality
print(my_module.my_favorite_number)

# random integer: a <= N <= b same as rang range(a, b+1)
random_integer = random.randint(1, 10)
print(random_integer)

# random float: 0.0 <= X < 1.0
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# Heads or Tails 1 or 0
Head_or_tail = random.randint(0, 1)
if Head_or_tail == 0:
    print("Tails")
else:
    print("Heads")

# Head_or_tail = random.choice(['Head', 'Tail'])
# print(Head_or_tail)
