import json
import os
class Task:
    def __init__(self, name: str, completed=False):
        self.name = name
        self.completed = completed
    def to_dict(self):
        return {
            "name" : self.name,
            "completed" : self.completed
        }
    def __str__(self):
        return f"{self.name} {'✅' if self.completed else '❌'}"
    
    def __repr__(self):
        return f"Task(name={self.name}, completed={self.completed})"

class TodoList:
    def __init__(self, filename: str):
        folder_path = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(folder_path, filename)
        self.tasks = self.load_data()
    def load_data(self):
        try:
            with open(f"{self.filename}.json", "r") as file:
                data = json.load(file)
                return [Task(item["name"], item["completed"]) for item in data]
        except FileNotFoundError:
            return []
    def save_data(self):
        with open(f"{self.filename}.json", "w") as file:
            data = [item.to_dict() for item in self.tasks]
            json.dump(data, file, indent=4)

    # --------------------------- #
    #           Helpers           #
    # --------------------------- #
    def check_index(self, user_index: int):
        index = user_index -1
        if 0 <= index < len(self.tasks):
            return index
        return None
    # --------------------------- #
    #             CRUD            #
    # --------------------------- #

    #CREATE
    def add_task(self, name: str):
        self.tasks.append(Task(name))
        self.save_data()
        return True
    
    #READ
    def get_tasks(self):
        return self.tasks
    
    #UPDATE
    def update_task(self, user_index: int, name: str = None, status: bool = None):
        index = self.check_index(user_index)
        if index is not None:
            if name is not None and name != "":
                self.tasks[index].name = name
            if status is not None:
                self.tasks[index].completed = status
            self.save_data()
            return True
        else:
            return False

    #DELETE
    def delete_task(self, user_index: int):
        index = self.check_index(user_index)
        if index is not None:
            self.tasks.pop(index)
            self.save_data()
            return True
        else:
            return False
    
