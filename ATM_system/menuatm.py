from atmclass import BankAccount
import os

def menu():
    app = BankAccount("bankacc")
    while True:
        os.system('cls')
        print("Welcome to the ATM!")
        print("1. See your balance")
        print("2. Make a deposit")
        print("3. Make a withdrawal")
        print("4. See your bank history")
        print("5. Exit")
    
        try:
            option = int(input("What do you wish to do?: "))
        except ValueError:
            input("You can only choose A NUMBER from the options listed above. Enter to go back ")
            continue
        match option:
            case 1:
                app.show_balance()
            case 2:
                app.deposit()
            case 3:
                app.withdraw()
            case 4:
                app.acc_data()
            case 5:
                break
            case _:
                input("Not a valid option. Enter to try again. ")

if __name__ == "__main__":
    menu()