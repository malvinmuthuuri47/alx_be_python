"""
This module implements a function that performs the division mathematical
operation
"""

def safe_divide(numerator: int, denominator: int) -> str:
    """
    This function performs division and raises an error depending on
    the parameters passed. If denominator is 0, a ZeroDivisionError
    exception is raised and if not, attempt to convert the argument to
    floats and catch a ValueError exception for non-numeric inputs.
    Otherwise, return an appropriate message for errors or the result
    for successful division.
    """
    try:
        res = float(numerator) / float(denominator)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {res}"
