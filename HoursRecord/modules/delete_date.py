def delete_date (data: dict) -> dict:
    # Delete an existing date from the records

    from datetime import datetime
    import os

    while True:
        # Clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Deleting date...\n")

        # Ask for date to delete
        try:
            date = input("Enter the date you want to delete (dd/mm/yyyy): ").strip()
            print()
            datetime.strptime(date, "%d/%m/%Y")
            if date not in data:
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

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete the record for {date}? (y/n): ").strip().lower()
    if confirm == 'y':
        del data[date]
        print(f"Record for {date} deleted.")
    else:
        print("Deletion cancelled.")

    print()
    input("Press Enter to continue...")
    return data