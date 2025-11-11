class Pets():
    def __init__(self, animals: list):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Siamese(Cat):
    def __init__(self, name, age, personality):
        super().__init__(name, age)
        self.personality = personality

    def display_personality(self):
        print(self.personality)

class SaraPets(Pets):
    def __init__(self, animals):
        super().__init__(animals)

    def display_animals(self):
        for animal in self.animals:
            print(f"{animal.name} is one of sara's pets.")



bengal_obj = Cat("John", 34)
chartreux_obj = Cat("Milly", 12)
siamese_obj = Cat("James", 42)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = SaraPets(all_cats)
sara_pets.display_animals()
sara_pets.walk()