import os
from data.save_and_load import load_data, save_data
from modules.menu import display_menu
from modules.verify_no_records import verify_no_records
from modules.add_date import add_date
from modules.view_records import view_records
from modules.edit_date import edit_date
from modules.delete_date import delete_date
from modules.view_summary import view_summary

def main():
    # Load data
    data = load_data()

    # Main loop
    while True:
        # Clear console
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

        except Exception as e:
            print(f"An error occurred: {e}")
            print()
            input("Press Enter to continue...")
            continue

        # Display menu and select action
        action = display_menu()

        # Verify if there are records
        if action in [2, 3, 4, 5] and verify_no_records(data):
            continue

        # 1 Add new date
        if action == 1:
            data = add_date(data)

        # 2 View records
        if action == 2:
            view_records(data)

        # 3 Edit date
        if action == 3:
            data = edit_date(data)

        # 4 Delete date
        if action == 4:
            data = delete_date(data)
        
        # 5 View summary
        if action == 5:
            view_summary(data)

        # 6 Exit
        if action == 6:
            print("Exiting program. Goodbye!")
            save_data(data)
            break
                
        # Save data
        save_data(data)


if __name__ == '__main__':
    main()