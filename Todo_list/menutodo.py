from todoclass import TodoList
import os

def menu():
    app = TodoList("tasks")
    while True:
        os.system('cls')
        print("Welcome to your TO-DO LIST!")
        print("1. Add task to do")
        print("2. See to-do list")
        print("3. Modify a task")
        print("4. Delete a task")
        print("5. Exit")

        try:
            option = int(input("What do you wish to do?: "))
        except ValueError:
            input("You can only choose A NUMBER from the options listed above. Enter to go back ")
            continue
        match option:
            case 1:
                name = input("Whats the name of the task?: ")
                app.add_task(name)
            case 2:
                app.show_tasks()
            case 3:
                app.update_task()
            case 4:
                app.delete_task()
            case 5:
                print("Goodbye!")
                break
            case _:
                input("Not a valid option. Enter to try again. ")


if __name__ == "__main__":
    menu()