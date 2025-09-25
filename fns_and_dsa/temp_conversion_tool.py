"""
This module implements logic to convert temperatures between Celcius and Fahrenheit,
using global variables to store conversion factors
"""

FAHRENHEIT_TO_CELCIUS_FACTOR = 5/9
CELCIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    """
    This function takes temperature in fahrenheit and returns the temperature
    converted to celcius
    """
    res = fahrenheit * FAHRENHEIT_TO_CELCIUS_FACTOR
    print(f"{fahrenheit} is {res}25\u00B0 C")

def convert_to_fahrenheit(celcius):
    """
    This function takes temperature in Celcius and returns the temperature
    converted to fahrenheit
    """
    res = celcius * CELCIUS_TO_FAHRENHEIT_FACTOR
    print(f"{celcius} is {res}25\u00B0 F")

def main():
    temp_var = float(input("Enter the temperature to convert: "))
    C_or_F = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")

    match C_or_F:
        case "C":
            convert_to_fahrenheit(temp_var)
        case "F":
            convert_to_celcius(temp_var)
        case _:
            raise Exception("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
