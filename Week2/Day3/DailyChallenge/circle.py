from math import pi

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
    
if __name__=="__main__":
    circle1 = Circle(diameter=10)
    print(circle1.compute_area())