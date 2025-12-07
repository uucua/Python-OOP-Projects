def header(text: str):
    print("=" *25)
    print(f"      {text.upper()}")
    print("=" *25)

def show_options():
    print("1. Add task to do\n2. See to-do list\n3. Modify a task\n4. Delete a task\n5. Exit")

def show_goodbye():
    print("\n👋 Goodbye! See you next time.")

def _print_status(text: str, success: bool):
    prefix = "✅ SUCCESS:" if success else "❌ ERROR:"
    print(f"{prefix} {text}")

def print_success(text:str):
    _print_status(text, success= True)

def print_error(text: str="Invalid task number. "):
    _print_status(text, success= False)

def print_tasks(task_list: list):
    if task_list:
        print("INDEX - NAME - COMPLETE?")
        for num, task in enumerate(task_list, 1):
            print(f"{num}. {task}")
    else:
        print("You currently have no tasks.")