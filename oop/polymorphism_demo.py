class Shape:
    def area(self):
        raise NotImplementedError("يجب تجاوز هذه الدالة في الكلاسات الفرعية")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)