class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2
    def perimetr(self):
        return self.radius * 2 * 3.14


Circle = Circle(10)
Circle = Circle.get_area(), Circle.perimetr()
print(Circle)









