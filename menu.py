def main_menu():
    print("1. File")
    # Prompt the user to enter a menu choice
    choice = input("Enter a menu choice: ")
    if choice == "1":
        file_menu()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


# Define a function to display the file menu
def file_menu():
    print("File Menu")
    print("1. Open")
    print("2. Save")
    print("3. Back to Main Menu")
    
    # Prompt the user to enter a menu choice
    choice = input("Enter a menu choice: ")

    # Call the appropriate function based on the user's choice
    if choice == "1":
        print("Open file");
    elif choice == "2":
        print("Save file");
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        file_menu()

main_menu();