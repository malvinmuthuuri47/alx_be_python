'''
This module is used to recommend the clothes a user will wear based on the weather they describe.

The pseudocode is as follows:
    START
    1. Prompt the user for weather input
    2. Check that the input matches the expected prompts:
        - If the input is ("sunny", "rainy", "cold"), make the following recommendations:
            -> Sunny -> Wear a t-shirt and sunglasses
            -> Rainy -> Don't forget your umbrella and a raincoat
            -> Cold -> Make sure to wear a coat and a scarf
        - If input doesn't match the expected conditions:
            -> Print an error message to the standard output
    END
'''

weather = str(input("What's the weather like today? (sunny/rainy/cold): ")).strip().lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
