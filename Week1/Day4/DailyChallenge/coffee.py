# Key => Drink Value: str => Price: float
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0,
}


def show_menu(menu_dict):
    for key, value in menu_dict.items():
        if not menu_dict:
            print("Menu is empty") 
        else:
            for key, value in menu_dict.items():
                print(f"{key.title()} - {value}₪")


def add_item(menu_dict):
    new_drink = str(input("enter a drink name: "))
    drink_price = float(input("what is the price? "))
    if new_drink in menu_dict.keys():
        print("drink already exists")
    else:
        menu_dict[new_drink] = drink_price
        print(f"{new_drink} added!")


def update_price(menu_dict):
    user_prompt = input("What drink would you like to update? ")
    if user_prompt in menu_dict.keys():
        price_update = float(input("Enter a new price: "))
        menu_dict[user_prompt] = price_update
        print("Price updated!")
        print(menu_dict)
    else:
        print("Item not found.")


def delete_item(menu_dict):
    item_to_delete = str(input("Which item would you like to delete? "))
    if item_to_delete in menu_dict.keys():
        del menu_dict[item_to_delete]
        print(f"{item_to_delete} deleted.")
        print(menu_dict)
    else:
        print("item not found")

lst_of_functions = [show_menu, add_item, update_price, delete_item]

def show_options():
    print("What would you like to do?")
    for i, f in enumerate(lst_of_functions):
        print(f"{i}. {f.__name__.replace('_', ' ').title()}")
    print(f"{len(lst_of_functions) + 1}. Exit")



def run_coffee_shop():
    while True:
        show_options()
        try: 
            prompt = int(input("Enter 1-5 to call a function: "))
        except ValueError:
            print("please enter a valid number.")

        if prompt == 1:
            show_menu(menu)
        elif prompt == 2:
            add_item(menu)
        elif prompt == 3:
            update_price(menu)
        elif prompt == 4:
            delete_item(menu)
        elif prompt == 5: 
            print('Goodbye!')
            break
        else:
            print('Invalid choice')

if __name__=='__main__':
    run_coffee_shop()

