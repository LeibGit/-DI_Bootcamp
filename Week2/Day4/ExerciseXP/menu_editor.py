from menu_manager import MenuManager

def load_manager():
    return MenuManager(r"menu.json")

def show_user_menu():
    manager = load_manager()
    while True:
        print("Program Menu:")
        print("Enter 1 to add_item: ")
        print("Enter 2 to remove_item: ")
        print("Enter 3 to view_menu: ")
        print("Enter 4 to add a valentines day item: ")
        print("Enter 5 to exit: ")
        user_input = int(input("Enter your number choise here: "))

        if user_input == 1:
            get_name = input("Enter the name of the item: ")
            get_price = int(input("Enter the price of the item: "))
            if get_price < 1:
                raise ValueError("Enter an positive interger for price and a string for name.")
            manager.add_item(name=get_name, price=get_price)
            manager.save_to_file()
            print(f"{get_name} added to the menu.")
        elif user_input == 2:
            get_name = input("Enter the name of the item: ")
            manager.remove_item(get_name)
            manager.save_to_file()
            print(f"Removed {get_name} from your menu.")
        elif user_input == 3:
            print(manager.view_menu())
        
        elif user_input == 4:
            get_name = input("Enter the name of the item: ")
            get_price = int(input("Enter the price of the item: "))
            if get_name[0].isupper():
                if get_name[0] == "V":
                    manager.add_item(name=get_name, price=get_price)
                    manager.save_to_file()
            else:
                print("First character needs to be capatalized and be 'V'!!!")
            print(f"{get_name} added to the menu.")

        elif user_input == 5:
            print("Menu changes have been saved.")
            print(manager.view_menu())
            break 
        else:
            print("please enter a valid input")
        

if __name__ == "__main__":
    print(show_user_menu())