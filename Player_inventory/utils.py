import os

def pause(message="Press enter to continue..."):
    input(message)

def ask_int(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            pause("Only numbers allowed. Press enter to try again")

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
            return float(input(f"{message}"))
        except ValueError:
            print("Error: Please enter a valid number (e.g. 7.60).")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')