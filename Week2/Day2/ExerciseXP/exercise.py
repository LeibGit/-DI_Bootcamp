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

# Exercise 2
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking.")
    
    def run_speed(self):
        calc = self.weight / self.age * 10
        print(f"{self.name} can run a speed of {calc}mph")
        return calc

    def fighting(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        try: 
            if self_power > other_power:
                print(f"{self.name} wins against {other_dog.name}")
            elif other_power > self_power:
                print(f"{other_dog.name} wins against {self.name}")
            else:
                print("Nobody wins, it is a tie.")
        except Exception as e:
            print(e)
        
dog1 = Dog("Joe", 12, 120)
dog2 = Dog("Milly", 14, 100)
dog1.bark()
dog1.run_speed()
dog1.fighting(dog2)