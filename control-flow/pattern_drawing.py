"""
This module implements logic to draw a square based on the user length using
nested loops

The pseudocode is as follows:
    1. Ask the user for input
    2. For every iteration of the row while row < user_num:
        - iterate num times drawing the square using the asterisk
"""

def draw_square():
    """
    This function takes the dimensions of a square and prints an asterisk
    corresponding to the square dimensions
    """
    square_dimensions = int(input("Enter the size of the pattern: "))

    row = 0
    while row < square_dimensions:
        for _ in range(square_dimensions):
            print("*", end="")
        print()
        row += 1

if __name__ == "__main__":
    draw_square()
