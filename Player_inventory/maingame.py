import os
from inventoryclass import Inventory

def maingame():
    player = Inventory("player")
    while True:
        os.system('cls')
        print("Welcome to the Inventory RPG")
        print("1. See your inventory")
        print("2. Add items to your inventory")
        print("3. Delete items from your inventory")
        print("4. See your inventory worth")
        print("5. Exit")

        try:
            option = int(input("What do you choose?: "))
        except ValueError:
            input("You can ONLY TYPE NUMBERS, Enter to go back: ")
            continue
        
        match option:
            case 1:
                player.show_items()

            case 2:
                name = input("Name of the item?: ")
                category = input("Category of the item?: ")
                while True:
                    try:
                        value = int(input("Value of the item?: "))
                    except ValueError:
                        input("You can only type numbers for the value. Enter to try again: ")
                        continue
                    break
                player.add_item(name, category, value)

            case 3:
                player.delete_item()
            
            case 4:
                print(player.get_total_value())
                input("Enter to go back: ")
            case 5:
                break
            case _:
                input("Not a valid option. Enter to try again. ")
                
if __name__ == "__main__":
    maingame()


