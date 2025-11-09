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