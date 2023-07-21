import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * (self.radius)
c = circle(int(input("Enter radius: ")))
print ("Area: ", c.area())
print ("Perimeter: ", c.perimeter())

    