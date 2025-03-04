# range function with for loop
for i in range(3):
    print(i)
print()

for number in range(1, 6):
    print(number)
print()

for number in range(1, 7, 2):
    print(number)
print()

# Gauss Challenge: Add up 1 to 100
print("Sum of 1 to 100:")
total_sum_1_to_100 = 0
for number in range(1, 101):
    total_sum_1_to_100 += number
print(total_sum_1_to_100)
