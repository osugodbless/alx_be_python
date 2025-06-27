import math

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        raise NotImplementedError("Derived classes to override this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
