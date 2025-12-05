import json
import os
class Task:
    def __init__(self, name: str, completed=False):
        self.name = name
        self.completed = completed
    def to_dict(self):
        task = {
            "name" : self.name,
            "completed" : self.completed
        }
        return task

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

    def confirmation(self, message: str):
        while True:
            confirm = input(f"{message} (Y/N): ").lower()
            if confirm == "y":
                return True
            elif confirm == "n":
                return False
            else:
                print("Please type a valid answer (Y/N)")
    
    def add_task(self, name: str):
        if self.confirmation(f"Are you sure you want to add '{name}'?"):
            print("Task added succesfully!")
            self.tasks.append(Task(name))
            self.save_data()
            input()
        else:
            print("The task wasn't added.")
            input()

    def show_tasks(self, mode="view"):
        if self.tasks:
            for num, item in enumerate(self.tasks, 1):
                print(f"{num}. {item.name}, Completed? {'✅' if item.completed == True else '❌'}")
            if mode != "used":
                input("Press enter to continue. ")
            return True
        else:
            print("You currently have no tasks.")
            if mode != "used":
                input("Press enter to continue. ")
            return False
    def get_index(self, mode: str):
        while True:
            try:
                if mode == "update":
                    opt = int(input("Type the number of the task you want to edit: "))
                elif mode == "delete":
                    opt = int(input("Type the number of the task you want to delete: "))
            except ValueError:
                print("You can only type NUMBERS")
                continue  
            if 1 > opt or opt > len(self.tasks):
                print("That task doesn't exist (Number too high or too low)")
                continue
            else:
                return opt-1
        
    def delete_task(self):
        if self.show_tasks("used"):
            task = self.get_index("delete")
            if self.confirmation(f"Are you sure you want to delete '{self.tasks[task].name}'?"):
                self.tasks.pop(task)
                self.save_data()
                input("Task deleted succesfully! Press enter to continue. ")
            else:
                input("The task wasn't deleted. Press enter to continue. ")
        else:
            input("There are no tasks to delete. Press enter to continue. ")
    
    def update_task(self):
        if self.show_tasks("used"):
            task = self.get_index("update")
            if self.confirmation(f"Are sure you want to edit '{self.tasks[task].name}'?"):
                name = str(input("New name? leave blank if you don't want to change it: "))
                status = str(input("Completed (Y/N)? leave blank if you don't want to change it: "))
                if name != "":
                    self.tasks[task].name = name
                if status != "":
                    if status.lower() == "y":
                        self.tasks[task].completed = True
                    elif status.lower() == "n":
                        self.tasks[task].completed = False
                self.save_data()
                input("Task edited succesfully! Press enter to continue. ")
            else:
                print("The task wasn't edited.")
                input()
        else:
            input("There are no tasks to edit. Press enter to continue. ")