import json

class MenuManager():
    def __init__(self, menu):
        self.menu_file = menu
        with open(menu, 'r') as file:
           restruant_menu = json.load(file) 
        self.menu = restruant_menu

    def add_item(self, name, price):  
        item_to_add = {
            'name': name,
            'price': price
        }
        self.menu["items"].append(item_to_add)
        return f"{item_to_add} added."
    
    def remove_item(self, name):
        for item in self.menu["items"]:
            if item["name"] == name:
                self.menu["items"].remove(item)
                return True
            else:
                continue
        return False
    
    def save_to_file(self):
        with open(self.menu_file, 'w') as file:
            json.dump(self.menu, file, indent=4)
        return "Menu updated"
                

if __name__=="__main__":
    test = MenuManager(r"menu.json")
    print(test.add_item("Cherries", 20))
    print(test.remove_item("pizza"))
    print(test.save_to_file())