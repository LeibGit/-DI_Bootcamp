from exercise import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)

    def train(self):
        self.bark()
        self.trained = True
        print(self.trained)
    
    def play(self, *dogs):
        dog_names = [dog.name for dog in dogs]
        try:
            print(f"{', '.join(dog_names)} all play together.")
        except Exception as e:
            print(e)

    def do_a_trick(self):
        if self.trained == True:
            try:
                trick = random.choice(tricks)
                print(f"{self.name} {trick}")
            except Exception as e:
                print(e)

tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]

dog1 = PetDog("Will", 12, 120)
dog2 = PetDog("Marie", 15, 190)
dog3 = PetDog("Shawn", 25, 130)

dog1.train()
dog1.play(dog2, dog2)
dog1.do_a_trick()

dog2.train()
dog2.play(dog1, dog3)
dog2.do_a_trick()

# Exercise 4

class Person():
    def __init__(self, first_name, age, last_name=''):
        self.first_name = first_name
        self.age = age
    
    def is_18(self):
        if self.age >= 18:
            print(f"{self.first_name} is 18 or over.")
            return True
        else:
            return False
    
class Family():
    def __init__(self, last_name, members=[]):
        self.last_name = last_name

    def born(self, first_name, age):
            person = {first_name = age}
            self.members.append(person)
