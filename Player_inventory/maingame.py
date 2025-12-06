import os
from inventoryclass import Inventory
from utils import pause, ask_int, ask_yes_no, ask_float, clear


def maingame():
    player = Inventory("player")
    while True:
        clear()
        print("Welcome to the Inventory RPG")
        print("1. See your inventory")
        print("2. Add items to your inventory")
        print("3. Delete items from your inventory")
        print("4. See your inventory worth")
        print("5. Exit")

        option = ask_int("What do you choose?: ")
        
        match option:
            case 1:
                clear()
                player.show_items()
                pause()

            case 2:
                clear()
                name = input("Name of the item?: ")
                category = input("Category of the item?: ")
                value = ask_float("Value?: ")
                player.add_item(name, category, value)
                pause("Succesfully added item! Enter to continue... ")

            case 3:
                clear()
                if player.show_items():
                    index = ask_int("Type the number of the item to delete: ")
                    if ask_yes_no("Are you sure you want to delete this item?"):  
                        if player.delete_item(index-1):
                            pause("The item was deleted succesfully. ")
                        else:
                            pause(f"The item with index {index} was not found. ")
                    else:
                        pause("Deletion cancelled. ")
            
            case 4:
                clear()
                total = player.get_total_value()
                if total == 0:
                    pause("You have no items, your inventory is worth $0. ")
                else:
                    pause(f"Total worth of your Inventory: ${total}. ")
            case 5:
                break
            case _:
                pause("Not a valid option. Enter to try again. ")
                
if __name__ == "__main__":
    maingame()
