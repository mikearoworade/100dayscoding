# Passing a function into another function
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


# Higher order function
def calculator(n1, n2, func):
    return func(n1, n2)


result = calculator(3, 2, add)
print(result)
