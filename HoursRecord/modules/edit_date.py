def edit_date(data: dict):
    # Edit an existing date in the records

    from datetime import datetime
    import os
    while True:
        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Editing date...\n")

        # Ask for confirmation
        print("1. Edit date")
        print("2. Cancel\n")
        try:
            option = int(input("Select an option (1, 2): "))
            # Validate option
            if option < 1 or option > 2:
                raise ValueError
        except ValueError:
            try:
                print("\nInvalid input, please try again.")
                input("Press Enter to continue...")
                date = None
                continue
            except EOFError:
                return data
        else:
            break

    # If option 2, return data unchanged and go back to main menu
    if option == 2:
        return data
    
    # If option 1, proceed to edit
    # Ask for the date to edit
    try:
        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Editing date...\n")

        # Ask for date to edit
        date = input("Enter the date you want to edit (dd/mm/yyyy): ").strip()
        print()
        datetime.strptime(date, "%d/%m/%Y")
        if date not in data:
            print("Date not found in records.")
            raise ValueError
    
    except ValueError:
        print('Invalid input, please try again.')
        input("Press Enter to continue...")
        return edit_date(data)

    # Call add_date to modify the entire date, first delete the existing date
    from modules.add_date import add_date
    return add_date(data, date)
