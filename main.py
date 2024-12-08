# app.py
import math


def add_numbers(a, b): # Missing type hints
    """Adds two numbers"""
    return a + b


def divide_numbers(a, b):  # Missing docstring
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def unused_function():
    pass  # Unused function to trigger an analysis warning


def main():
    result_add = add_numbers(5, 10) 
    result_divide = divide_numbers(10, 2)
    result_error = divide_numbers(10, 0)
    print(f"The addition result is: {result_add}") 
    print(f"The division result is: {result_divide}")
    print(f"The error case result is: {result_error}")


main() # Direct call to main, not in "if __name__ == '__main__'"
