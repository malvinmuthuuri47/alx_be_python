"""
1. Ask the user for their age through the command line
2. Deduce the year they were born from their age
3. Calculate how old the user will be in 2050 from the birth year.

Pseudocode:
    - Ask the user for their age
    - Add 27 to their current age
    - Print the results
"""

current_age = int(input("How old are you? "))

future_age = current_age + 27

print(f"In 2050, you will be {future_age} years old.")
