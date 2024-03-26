from math import pi, sqrt


# абстрактный класс
class Shape:
    def __init__(self, *args): pass

    def area(self, *args): pass  # ? Вычисление площади фигуры без знания типа фигуры в compile-time

    def perimetr(self, *args): pass


# Exception, если ввели неверное соотношение сторон треугольника
class TriangleException(Exception):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __str__(self):
        return f"Недопустимые значения сторон. Сумма любых двух сторон треугольника всегда больше любой стороны."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        return pi * self.radius**2


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        if a + b > c and a + c > b and b + c > a:
            self.a, self.b, self.c = a, b, c
        else:
            raise TriangleException(a, b, c)

    def area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

    def right_triangle(self):
        l1 = [self.a, self.b, self.c]
        l1.sort()
        return l1[0]**2 + l1[1]**2 - l1[2]**2 < 0.00000001  # на случай с плавающей точкой


