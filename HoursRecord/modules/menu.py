def display_menu() -> int:
    # Display the main menu and get user option
    
    # Clear console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display menu options
    print("Options Menu:")
    print()
    print("1. Add date")
    print("2. View records")
    print("3. Edit date")
    print("4. Delete date")
    print("5. View summary")
    print("6. Exit")

    # Get user option
    while True:
        try:
            option = int(input("\nSelect an option: "))
            print()

            # Validate option
            if option < 1 or option > 6:
                raise ValueError
            
        except ValueError:
            try:
                print("\nInvalid input, please try again.")
                input("Press Enter to continue...")
                continue
            except EOFError:
                return 6
        
        except EOFError:
            return 6

        # Return valid option
        else:
            return option
