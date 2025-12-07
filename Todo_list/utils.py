import os

def pause(message : str ="Press enter to continue..."):
    input(message)

def ask_string(message: str, optional : bool = False):
    while True:
        text = input(message).strip()
        if not text and not optional:
            print("Error: This field cannot be empty.")
            continue
        return text
        

def ask_int(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("❌ ERROR: Only numbers allowed. ")

def ask_yes_no(message: str):
    while True:
        choice = input(f"{message} (Y/N): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid option, type 'Y' for Yes or 'N' for No")

def ask_float(message: str):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Please enter a valid number (e.g. 7.60).")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_optional_bool():
    status = input("Completed?: (Y/N) Leave blank if you don't want to edit. ").strip().lower()
    if status == "y":
        return True
    elif status == "n":
        return False
    else:
        return None
    

