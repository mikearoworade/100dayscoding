# Defining and calling a function
# Functions are block of codes that runch when called
def my_function():
    print("Hello World")


my_function()
print()


# Arguments: information can be passed into functions as arguments
def your_name(firstname):
    print(firstname + " Aroworade")


your_name("Ayodele")


def fullname(firstname, lastname):
    print("My name is " + firstname + " " + lastname)


fullname("Ayodele", "Aroworade")


# Arbitrary Arguments, *args
def my_family(*family):
    print("The youngest child of my family is " + family[-1])
    print()


my_family("Sunday", "Monday", "Tuesday", "Wednesday")
