"""
This module defines a function that performs basic arithmetic operations.
"""

def perform_operation(num1, num2, operation):
    """
    This function takes in three params:
        - num1 -> first number
        - num2 -> second number
        - operation -> the arithmetic operation to perform
    The function performs the maths operation based on the input and returns the result
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'ZeroDivisionError: division by zero'
        else:
            return num1 / num2
    else:
        return 'You entered the wrong operation'
