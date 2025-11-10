class Farm():
    def __init__(self, name: str, animals: dict):
        self.name = name
        self.animals = animals

    def add_animal(self, animal_type, count=1):
        for animal, c in self.animals.items():
            if animal_type in self.animals.keys():
                self.animals[animal_type] = c + count
            else:
                self.animals[animal_type] = count
        print(self.animals)

    def get_info(self):
        print(f"{self.name}:")
        for animal, count in self.animals.items():
            print(f"{animal}: {count}")
        print("E-I-E-I-O")

some_farm = Farm("Some Farm", {'cow': 1, 'pig':3, 'horse': 2})
some_farm.add_animal("cow", 5)
some_farm.get_info() 