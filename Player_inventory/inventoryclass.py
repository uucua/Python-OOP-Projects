import os
import json

class Item:
    def __init__(self, name: str, category: str, value: int):
        self.name = name
        self.category = category
        self.value = value
    def to_dict(self):
        item = {
            "name":self.name,
            "category":self.category,
            "value":self.value
        }
        return item

class Inventory:
    def __init__(self, filename : str):
        folder_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(folder_path, filename)
        self.items = self.load_data()

    def load_data(self):
        try:
            with open(f"{self.filename}.json", "r") as file:
                data = json.load(file)
                return [Item(item["name"], item["category"], item["value"]) for item in data]
        except FileNotFoundError:
            return []
    
    def save_data(self):
        with open(f"{self.filename}.json", "w") as file:
            data = [item.to_dict() for item in self.items]
            json.dump(data, file, indent=4)
    
    def show_items(self, mode="view"):
        if self.items:
            for num, item in enumerate(self.items, 1):
                print(f"{num}. Name: {item.name} Category: {item.category} Value: {item.value}")
            if mode == "view":
                input("Enter to go back... ")
            return True
        else:
            input("Your inventory has no items!. Enter to go back: ")
            return False

    def add_item(self, name: str, category: str, value: int):
        self.items.append(Item(name, category, value))
        self.save_data()
        input("Successfully created item! Enter to go back: ")

    def get_total_value(self):
        sum = 0
        if self.items:
            for item in self.items:
                sum += item.value
            return f"The total value of your inventory is ${sum}"
        else:
            return f"You currently have no items, your inventory value is $0"

    def delete_item(self):
        if self.show_items("used"):
            while True:
                try:
                    opt = int(input("Type the number of the item to delete: "))
                except ValueError:
                    input("You can only TYPE NUMBERS!. Enter to go back: ")
                if opt > len(self.items) or opt < 1:
                    input("That item doesn't exist! make sure to choose a valid number. Enter to go back: ")
                    continue
                else:
                    self.items.pop(opt-1)
                    self.save_data()
                    input("Item deleted successfully! Enter to go back: ")
                    break
        else:
            return