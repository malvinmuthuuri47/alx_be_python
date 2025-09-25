"""
This module creates a simple shopping list interface that allows users to add items, view
the current list, and remove items
"""

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_item = input("Enter the item to add: ").lower().strip()
            shopping_list.append(user_item)
            print(f"You just added {user_item} to the list")
            print()
        elif choice == '2':
            # Prompt for and remove an item
            user_item = input("Enter an item you want to remove: ").lower().strip()
            try:
                shopping_list.remove(user_item)
                print(f"You just removed {user_item} from the list")
                print()
            except Exception as e:
                print(e)
                print()
        elif choice == '3':
            # Display the shopping list
            print("The list items are: ")
            for list_item in shopping_list:
                print("-", list_item)
            print()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
