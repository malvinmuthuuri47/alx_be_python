"""
This is a python script meant to perform arithmetic operations
on a set of numbers
"""
number1 = 10
number2 = 5

operations = {
            "Addition": lambda x, y: x + y,
            "Subtraction": lambda x, y: x - y,
            "Multiplication": lambda x, y: x * y
        }
for operand_name, func in operations.items():
    result = func(number1, number2)
    print(f"{operand_name} of {number1} and {number2} is {result}")
