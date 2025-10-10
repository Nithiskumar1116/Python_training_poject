import json
import os

DATA_FILE = "bank_data.json"

def load_data():
    """Load account data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        return data
    return {}

def save_data(data):
    """Save account data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_account(data):
    """Add a new account."""
    name = input("Enter account holder name: ").strip()

    if name in data:
        print(f"Account for '{name}' already exists!")
        return data

    pin = input("Enter 4-digit PIN: ").strip()
    balance = float(input("Enter initial balance: "))

    data[name] = {
        "account_holder": name,
        "pin": pin,
        "balance": balance
    }

    print(f"\nAccount for '{name}' added successfully!")
    return data


# --- Main program ---
if __name__ == "_main_":
    data = load_data()
    data = add_account(data)
    save_data(data)
    print("\nCurrent data in file:")
    print(load_data())