import math 
import random
import string

chars = string.ascii_lowercase

pi = math.pi
class Circle():
    def __init__(self, radius: float):
        self.radius = radius
    
    def compute_perimeter(self):
        perimeter = self.radius*2*pi
        print(perimeter)
        return perimeter
    
    def compute_area(self):
        area = pi*self.radius**2
        print(area)
        return area

    def print_defintion():
        print("A circle is the set of all points in a plane that are at an equal distance (radius) from a fixed point called the center.")
circle_1 = Circle(3)
circle_2 = Circle(5.2)

circle_1.compute_area()
circle_2.compute_area()

circle_1.compute_perimeter()
circle_2.compute_perimeter()

class MyList():
    def __init__(self, letters: list):
        self.letters = letters
    
    def reverse_list(self):
        reversed_list = list(reversed(self.letters))
        print(reversed_list)
        return reversed_list
    
    def sorted_list(self):
        sorted_list = sorted(self.letters)
        print(sorted_list)
        return sorted_list

    def new_list(self):
        new_list = []
        for l in self.letters:
            new_list.append(random.choice(chars))
        print(new_list)

list_1 = MyList(['h', 'w', 'y', 'g'])

list_1.reverse_list()
list_1.sorted_list()
list_1.new_list()