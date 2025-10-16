import math

class Shape:
    def area(self):
        print("Area method not implemented for base Shape.")
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# 1. Polymorphism, Circle and Rectangle use the same method Area from Shape
# 2. Reusing code, more efficient
# 3. Simply add another class reusing the same Area from Shape, refer to line 25

if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(4, 6)
    t = Triangle(3, 8)
    print(f"Circle area: {c.area():.2f}")
    print(f"Rectangle area: {r.area():.2f}")
    print(f"Triangle area: {t.area():.2f}")
