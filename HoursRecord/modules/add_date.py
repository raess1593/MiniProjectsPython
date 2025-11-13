def add_date(data: dict, date: str = None) -> dict:
    # Add a new date to the records

    import os
    from datetime import datetime

    while True:
        try:
            # Clear console
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Editing date...\n")

            # Date
            if date is None:
                date = input("Enter a date (dd/mm/yyyy): ").strip()
                datetime.strptime(date, "%d/%m/%Y")
                if date in data:
                    raise ValueError("Date already exists")

            # Hours
            hours = int(input("Number of hours (0-24): "))
            if not 0 <= hours <= 24:
                raise ValueError("Hours out of range")

            # Rating
            rating = int(input("Evaluate the day (1-5): "))
            if not 1 <= rating <= 5:
                raise ValueError("Rating out of range")

        except ValueError:
            try:
                print("\nInvalid input, please try again.")
                input("Press Enter to continue...")
                continue
            except EOFError:
                return data

        except EOFError:
            return data

        else:
            data[date] = {"hours": hours, "rating": rating}
            print(f"\nRecord added for {date}")
            input("Press Enter to continue...")
            break

    return data