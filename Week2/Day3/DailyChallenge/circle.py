from math import pi, sqrt
import turtle

class Circle():
    def __init__(self, radius=None, diameter=None):
        if (radius is not None and diameter is not None) or (radius is None and diameter is None):
            raise ValueError("Either Radius or Diameter has to be above zero, not both and not neither:") 
        self.radius = radius
        self.diameter = diameter
    

    def compute_area(self):
        if self.radius is not None:
            area = pi*self.radius**2
            return area
        else:
            area = 1/4*pi*self.diameter**2
            return area

    def __str__(self):
        return self.diameter, self.radius
    
    def __add__(self, other):
        if isinstance(other, Circle):
            total_area = self.compute_area() + other.compute_area()
            radius = sqrt(total_area/pi)
            return radius
        else:
            raise ValueError("Other circle added is not an instance.")
        
    def __gt__(self, other):
        if isinstance(other, Circle):
            if self.compute_area() > other.compute_area():
                return f"{self.compute_area()} is greater than {other.compute_area()}"
            elif self.compute_area() < other.compute_area():
                return f"{self.compute_area()} is less than {other.compute_area()}"
            else:
                return "They have the same area."
            
    def __eq__(self, other):
        if isinstance(other, Circle):
            if self.compute_area() == other.compute_area():
                return "They are equal."
            else:
                return "they are not equal."
        
    
    def __lt__(self, lst):
        return self.compute_area() < lst.compute_area()

    def draw_cirle(self):
        return turtle.circle(self.compute_area())
    
        
if __name__=="__main__":

    circle1 = Circle(diameter=10)
    circle2 = Circle(radius=10)
    circle3 = Circle(radius=10)
    circle4 = Circle(diameter=24)
    list_of_circles = [circle1, circle2, circle3, circle4]
    print(circle1.compute_area())
    print(circle1.__str__())
    print(circle1.__add__(circle2))
    print(circle1.__gt__(circle2))
    print(circle1.__eq__(circle2))
    print(sorted(list_of_circles))
    print(circle3.draw_cirle())