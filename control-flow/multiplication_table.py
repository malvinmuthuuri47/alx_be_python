"""
This module implements logic to generate a multiplication table for a given number.

The pseudocode for this function is as follows:
    1. Ask the user to enter a number
    2. Take the number and generate a multiplication table from 1 to 10 for that
       number.
"""

def num_multiplication_table():
    number = int(input("Enter a number to see its multiplication table: "))

    for multiplier in range(1, 10+1):
        result = number * multiplier
        print(f"{number} * {multiplier} = {result}")

if __name__ == "__main__":
    num_multiplication_table()
