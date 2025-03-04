# While loop
i = 1
while i < 4:
    print(i)
    i += 1
print()

# Break
i = 1
while i < 6:
    print(i)
    if i == 2:
        break
    i += 1
print()

# Continue
i = 0
while i < 4:
    i += 1
    if i == 2:
        continue
    print(i)
print()

# else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# while not
i = 0
while not i == 3:
    print(i)
    i += 1
