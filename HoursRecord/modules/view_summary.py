def view_summary(data: dict) -> None:
    # View summary of records in the data
    # Top 3, streak, total and average

    from datetime import datetime
    
    # Clear console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print("View Summary:")
    
    # Top 3
    sorted_items = sorted(data.items(), key=lambda item: item[1]['hours'])
    dates = [item[0] for item in sorted_items]
    hours = [item[1]['hours'] for item in sorted_items]

    # Display Top 3
    print("\n===================================")
    print("\nTop Recorded Hours:")
    print(f"Gold: {dates[-1]} {hours[-1]}")
    if len(hours) >= 2:
        print(f"Silver: {dates[-2]} {hours[-2]}")
        if len(hours) >= 3:
            print(f"Bronze: {dates[-3]} {hours[-3]}")

    # Streak
    sorted_dates = sorted(data.keys(), key=lambda date: datetime.strptime(date, "%d/%m/%Y")) 
    streak = 0
    max_streak = 0
    previous_date = None
    for date_str in sorted_dates:
        current_date = datetime.strptime(date_str, "%d/%m/%Y")
        if previous_date and (current_date - previous_date).days == 1:
            streak += 1
        else:
            streak = 1
        max_streak = max(max_streak, streak)
        previous_date = current_date

    
    print("\n===================================")
    print(f"\nLongest Streak of Consecutive Days: {max_streak} days")

    # Total
    print("\n===================================")
    print(f"\nTotal amount of hours: {sum(hours)}")
    print("Keep working! Stay hard!")

    # Average
    ratings = [details['rating'] for details in data.values() if 'rating' in details]

    average = int(sum(ratings)/len(ratings), 0) if ratings else 0

    print("\n===================================")
    print(f"\nRating average: {average}")
    
    if average >= 4:
        print("Excellent work! Keep it up!")
    elif average >= 3:
        print("Good job! You can do even better!")
    elif average >= 2:
        print("Not bad, but there's room for improvement.")
    else:
        print("Let's try to improve next time!")

    input("\nPress Enter to return to the menu...")