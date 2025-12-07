from todoclass import TodoList
from utils import pause, ask_int, ask_yes_no, clear, ask_optional_bool, ask_string
from views import print_tasks, header, show_options, print_success, print_error

#CREATES A LIST THEN PRINTS OUT EVERY ITEM IN IT
def refresh_view(app):
    clear()
    tasks = app.get_tasks()
    print_tasks(tasks)
    return tasks

def menu():
    app = TodoList("tasks")
    while True:
        clear()
        header("TO-DO LIST")
        show_options()

        option = ask_int("What do you wish to do?: ")
       
        match option:
            #---------------#
            #      ADD      #
            #---------------#
            case 1:
                clear()

                name = ask_string("Whats the name of the task?: ", optional=False)
                app.add_task(name)

                print_success("Task added.")
                pause()
            
            #---------------#
            #      READ     #
            #---------------#
            case 2:

                refresh_view(app)
                pause()
                
            #---------------#
            #     UPDATE    #
            #---------------#
            case 3:
                tasks = refresh_view(app)
                if tasks:
                    user_index = ask_int("Index of the task to edit: ")

                    name = ask_string("New name? (blank = skip): ", optional=True)
                    status  = ask_optional_bool()

                    if app.update_task(user_index,name,status):
                        print_success("Task updated.")
                    else:
                        print_error()
                pause()
                
            #---------------#
            #     DELETE    #
            #---------------#
            case 4:
                tasks = refresh_view(app)
                if tasks:
                    user_index = ask_int("Index of the task to delete: ")
                    confirm = ask_yes_no("Are you sure you want to delete this task?")
                    if confirm:
                        if app.delete_task(user_index):
                            print_success("Task deleted.")
                        else:
                            print_error()
                    else:
                        print_success("Deletion cancelled")
                pause()

            #BREAK
            case 5:
                print("Goodbye! ")
                break
            #ERROR
            case _:
                print_error("Invalid option.")
                pause()


if __name__ == "__main__":
    menu()