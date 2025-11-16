"""
1. Ask User how many players are playing
2. For each user prompt them to create there character getting name and age of character
3. Output all characters into a json file with all different character attributes
4. Each character will have six attributes (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma)
5. Scores for attributes are determended randomly. You role 6-sided dice and record the sum of the largest three dice
6. This is done 6 times, once for each attribute
7. Character class should be in charge of creating characters
8. Game class should be in charge of how many time a character gets instantiated and exporting the data in json
"""
import random
import json

def define_attributes():
    count = 0
    dice_values = []
    while count < 4: 
        dice_values.append(random.choice([1, 2, 3, 4, 5, 6]))
        count += 1
    min_val = min(dice_values)
    dice_values.remove(min_val)
    sum_val = sum(dice_values)
    return sum_val

class Character():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.strength = define_attributes()
        self.dexterity = define_attributes()
        self.constitution = define_attributes()
        self.intelligence = define_attributes()
        self.wisdom = define_attributes()
        self.charisma = define_attributes()
    
    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
        }
    
class Game():
    def __init__(self):
        self.players = {}

    def create_players(self):
        get_player_amt = int(input("Enter the amount of players: "))

        for i in range(1, get_player_amt + 1):
            get_name = input("Enter character name: ")
            get_age = input("Enter the player age: ")
            char = Character(get_name, get_age)
            self.players[i] = char.to_dict()

    def save_to_json(self):
        with open('player.json', 'w') as file:
            json.dump(self.players, file, indent=4)
        print("Saved players")

def main():
    game = Game()
    game.create_players()
    game.save_to_json()

if __name__ == "__main__":
    main()