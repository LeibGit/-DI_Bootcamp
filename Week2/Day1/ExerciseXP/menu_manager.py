# menu_manager.py

class MenuManager:
    def __init__(self):
        # menu is a list of dictionaries
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                print("Item already in menu, Add an original one.")
        new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_dish)
        print(self.menu)
        
    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"] == name:
                # Update the existing dictionary in-place
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"{name} updated successfully!")
                break  # Stop once the item is found
        else:
            # This runs if no break occurred (item not found)
            print("You can only update an item that exists.")
        print(self.menu)


    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"] ==  name:
                self.menu.remove(dish)
            else:
                continue
        print(self.menu)

some_restruant = MenuManager()
some_restruant.add_item(name="Choclate", price="20", spice="A", gluten=True)
some_restruant.update_item(name="Choclate", price="10", spice="A", gluten=False)
some_restruant.remove_item(name="Choclate")