import random


# for each suit in a list map create an element of that suit 
# for each differrent value in values


class Card:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    values = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    def __init__(self, suit, value):
        if suit not in Card.suits:
            raise ValueError(f"Invalid suit")
        
        elif value not in self.values:
            raise ValueError(f"Invalid suit")
        
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
    

deck = [Card(value, suit) for value in values for suit in suits]
print(deck)

class Deck:
    def __init__(self):
        pass 

    def shuffle_cards(self):
        pass