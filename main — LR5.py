print("Добрый день")
print("Лабораторная работа 5")
import math
class Shape:
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area() должен быть определен в дочернем классе.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Созданем объекты и задаем значения
shape = Shape()
circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

#print (circle)

# Подсчет площади объектов
try:
    print(shape.calculate_area())
except NotImplementedError as s:
    print(s)

print(f"Площадь круга: {circle.calculate_area()}")
print(f"Площадь прямоугольника: {rectangle.calculate_area()}")
print(f"Площадь квадрата: {square.calculate_area()}")