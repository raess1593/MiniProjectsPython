def verify_no_records(data: dict) -> bool:
    # Verify if there are no records
    if not data:
        print("No records found. Please add a date first.")
        input("Press Enter to continue...")
        return True
    return False