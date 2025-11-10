class Farm():
    def __init__(self, name: str, animals: dict):
        self.name = name
        self.animals = animals

    def add_animal(self, **kwargs):
        for animal, count in kwargs.items():
            if animal in self.animals:
               self.animals[animal] += count
            else:
                self.animals[animal] = count
        print(self.animals)

    def get_info(self):
        print(f"{self.name}:")
        for animal, count in self.animals.items():
            print(f"{animal}: {count}")
        print("E-I-E-I-O")

    def get_animal_type(self):
        animal_types = []
        for key in self.animals.keys():
            animal_types.append(key)
        print(sorted(animal_types))
        return animal_types

    def get_short_info(self):
        for i in self.get_animal_type():
            print(f"McDonald’s farm has {i}'s")
    
some_farm = Farm("Some Farm", {'cow': 1, 'pig':3, 'horse': 2})
some_farm.add_animal(goose=4, Monkey=1, cow=2)
some_farm.get_info() 
some_farm.get_animal_type() 
some_farm.get_short_info() 