# Multiple if statement
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? "))
    if age <= 12:
        print("Child Tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth Tickets are $7.")
        bill = 7
    # elif age >= 45 and age <= 55:
    elif age >= 45 & age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult Tickets are $12.")
        bill = 12

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No: ")
    if wants_photo == "y":
        # Add 3 dollar to bill
        bill += 3

    print("Your final bill is", bill)
else:
    print("Sorry you have to grow taller before you can ride.")
