import math

# Base class
class Shape:
    def area(self):
        """
        Base method to calculate area.
        This method is intended to be overridden by derived classes.
        """
        raise NotImplementedError("Subclasses must override the area() method.")

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Constructor for Rectangle class.
        
        :param length: Length of the rectangle.
        :param width: Width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the area of a rectangle.
        
        :return: Area of the rectangle (length × width).
        """
        return self.length * self.width

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """
        Constructor for Circle class.
        
        :param radius: Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the area of a circle.
        
        :return: Area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
