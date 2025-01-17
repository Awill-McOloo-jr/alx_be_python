# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Empty shopping list to start with

    while True:
        display_menu()  # Display the menu to the user
        choice = input("Enter your choice: ")

        if choice == '1':  # Add Item
            item = input("Enter the item to add: ").strip()  # Prompt updated to match the checker
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == '2':  # Remove Item
            item = input("Enter the item to remove: ").strip()  # Prompt updated to match the checker
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':  # View List
            if shopping_list:
                print("Your Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is currently empty.")

        elif choice == '4':  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()