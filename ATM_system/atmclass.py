import os
import json

class BankAccount:
    def __init__(self, filename):
        folder_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(folder_path, filename)

        data = self.load_data()

        if data:
            self.balance = data["balance"]
            self.history = data["history"]
        else:
            self.balance = 1000
            self.history = ["Account created with initial balance: 1000$"]

    def load_data(self):
        try:
            with open(f"{self.filename}.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        
    def save_data(self):
        data = {
            "balance": self.balance,
            "history": self.history
        }
        with open(f"{self.filename}.json", "w") as file:
            json.dump(data, file, indent=4)

    def show_balance(self, mode="view"):
        print(f"Your balance is: ${self.balance}")
        if mode != "used":
            input("Enter to go back: ")

    def get_number(self, message: str):
        while True:
            try:
                amount = int(input(f"How much do you want to {message}?: "))
            except ValueError:
                input("You can only type NUMBERS.")
                continue
            if amount <= 0:
                input(f"You can't {message} 0 or a negative amount. Enter to go back")
                break
            if message == "withdraw" and amount > self.balance:
                input("You CAN'T withdraw more mone than what you have! ")
                continue
            else:
                return amount

    def deposit(self):
        self.show_balance("used")
        amount = self.get_number("deposit")
        if amount:
            self.balance += amount
            self.history.append(f"Deposit, ${amount}")
            self.save_data()
            input("The deposit was successful! Enter to go back: ")
        else:
            return

    def withdraw(self):
        self.show_balance("used")
        amount = self.get_number("withdraw")
        if amount:
            self.balance -= amount
            self.history.append(f"Withdrawal, ${amount}")
            self.save_data()
            input("The withdrawal was successful! Enter to go back: ")
        else:
            return
    def acc_data(self):
        self.show_balance("used")
        for num, item in enumerate(self.history, 1):
            print(f"{num}. {item}")
        input("Enter to go back... ")
        

        
