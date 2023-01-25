# Calculator
from art import logo


# Add
def add(a, b):
    return a + b


# Subtract
def subtract(a, b):
    return a - b


# Multiply
def multiply(a, b):
    return a * b


# Divide
def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("what is the first number? "))
    continue_flag = 'y'
    while continue_flag == 'y':
        for key in operations:
            print(key)

        symbol = input("pick an operation: ")

        num2 = float(input("what is the next number? "))

        calc_func = operations[symbol]
        result = calc_func(num1, num2)

        print(f"{num1} {symbol} {num2} = {result}")

        continue_flag = input(f"Type 'y' to continue calculating from {result}, type 'n' to start a new calculation: ")
        num1 = result
        if continue_flag == 'n':
            calculator()


calculator()