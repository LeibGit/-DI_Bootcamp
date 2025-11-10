# Exercise 1
class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def find_oldest_cat(cat1, cat2, cat3):
        list_of_cats = [cat1, cat2, cat3]
        ages = []
        for cat in list_of_cats:
            ages.append(cat.age)
        print(max(ages))
            

cat1 = Cat("James", 90)
cat2 = Cat("Rio", 65)
cat3 = Cat("Coffee", 5)

Cat.find_oldest_cat(cat1=cat1, cat2=cat2, cat3=cat3)

# Exercise 2
class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high.")

    def compare_sizes(dog_1, dog_2):
        if dog_1.height > dog_2.height:
            print(f"{dog_1.name} is bigger than {dog_2.name}")
        elif dog_1.height == dog_2.height:
            print(f"{dog_1.name} and {dog_2.name} are the same size.")
        else:
            print(f"{dog_2.name} is bigger than {dog_1.name}")
davids_dog = Dog("Joe", 120)
sarahs_dog = Dog("Sam", 120)

Dog.bark(davids_dog)
Dog.bark(sarahs_dog)

Dog.jump(davids_dog)
Dog.jump(sarahs_dog)

Dog.compare_sizes(dog_1=davids_dog, dog_2=sarahs_dog)

class Song():
    def __init__(self, lyrics: list):
        self.lyrics = lyrics
    
    def sing_song(self):
        for i in self.lyrics:
            print(i)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

Song.sing_song(stairway)

class Zoo():
    def __init__(self, zoo_name, animals: list):
        self.zoo_name = zoo_name
        self.animals = animals

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("This animal is already in your zoo.")
        else:
            self.animals.append(new_animal)

    def get_animals(self):
        for i in self.animals:
            print(i)

    def sell_animal(self, animal_to_sell):
        if animal_to_sell in self.animals:
            self.animals.remove(animal_to_sell)
        else:
            print("this animal is not in your zoo.")

    def sort_animals(self):
        grouped = {}
        for animal in self.animals:
            if animal[0] not in grouped.keys():
                first_letter = animal[0]
                grouped[first_letter] = []
            # appending animals with that key letter
            grouped[first_letter].append(animal)
        print(sorted(grouped.items()))
        self.groups = sorted(grouped.items())
        return sorted(grouped.items())
        
    def get_groups(self):
        for key, value in self.groups:
            print(f"{key}: {value}")
            
# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari", [])

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_groups()