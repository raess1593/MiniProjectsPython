from pathlib import Path
import json

# Define paths
BASE = Path(__file__).resolve().parent
RECORDS = BASE / "records.json"

def save_data(data):
    # Save data to JSON file
    # Ensure directory exists
    RECORDS.parent.mkdir(parents=True, exist_ok=True)
    
    # Write data to file
    with RECORDS.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load_data():
    # Load data from JSON file
    try:
        with RECORDS.open("r", encoding="utf-8") as f:
            return json.load(f)
        
    except FileNotFoundError:
        # If file does not exist, create it with empty dict
        with RECORDS.open("w", encoding="utf-8") as f:
            json.dump({}, f)
        return {}
    
    except json.JSONDecodeError:
        # If JSON is corrupted, reset to empty dict
        with RECORDS.open("w", encoding="utf-8") as f:
            json.dump({}, f)
        return {}

    