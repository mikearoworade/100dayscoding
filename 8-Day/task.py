# Void function
def greet():
    print("Hello World")
    print("How do you do?")
    print("Isn't the weather nice?")


greet()
print()


# Function that allows 1 input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Michael")
print()


# Positional Argument Vs Keyword Argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like at {location}")


# Positional Argument
greet_with("Michael", "Victoria Island")
print()


# Keyword argument
greet_with(location="United Kingdom", name="Michael Aroworade")
print()
