import os
import json

class Item:
    def __init__(self, name: str, category: str, value: float):
        self.name = name
        self.category = category
        self.value = value
    def to_dict(self):
        return {
            "name":self.name,
            "category":self.category,
            "value":self.value
        }

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
    
    def show_items(self):
        if self.items:
            for num, item in enumerate(self.items, 1):
                print(f"{num}. Name: {item.name} Category: {item.category} Value: {item.value}")
            return True
        else:
            return False

    def add_item(self, name: str, category: str, value: float):
        self.items.append(Item(name, category, value))
        self.save_data()

    def get_total_value(self):
        return sum(item.value for item in self.items)
    
    def delete_item(self, index: int):
        if 0 <= index < len(self.items): # Validating index existence
            self.items.pop(index)
            self.save_data()
            return True # Success, deleted item
        else:
            return False # Error, item doesn't exist