calc_art = (r""" _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")


# TODO: Write out the functions: add, subtract, multiply and divide
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO: Add the operation into a dictionary. Keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations
# print(operations["*"](4, 8))


def calculator():
    print(calc_art)
    should_continue = True
    num1 = float(input("What is the first number? "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer} or 'n' to end: ").lower()
        if continue_calc == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
