'''
This module implements a calculator program with the match case introduced in python 3.10

The pseudocode is as follows:
    START
    1. Prompt the user for input:
        - num1 and num2
    2. Prompt the user to select the mathematical operation they want to perform
    3. Based on the maths operation:
        - If the operation is not division, allow the num2 to be 0
        - If the operation is division, raise an error and print it to the user
          saying that division by zero isn't possible because of the denominator
    4. Perform the maths operation and then return the results to the user using
       the print function.
    END
'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = str(input("Which operation do you want to perform? (+, -, *, /): "))

if operation == '+':
    result = num1 + num2
    print(f"The result is {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result is {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result is {result}")
elif operation == '/':
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"The result is {result}")
else:
    print("Wrong Operation")
