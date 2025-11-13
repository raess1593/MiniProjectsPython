def view_records(data: dict) -> None:
    # View all records saved

    # Clear console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("View Records:")
    
    # Display all records
    for date, details in data.items():
        print(f"\nDate: {date}\n Hours: {details['hours']}\n  Rating: {details['rating']}\n")
    input("Press Enter to return to the menu...")

    