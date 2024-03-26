from shapes import Circle, Triangle, TriangleException


if __name__ == '__main__':
    print(Circle(10).area())
    print(Triangle(3, 4, 5).area())
    try:
        print(Triangle(3, 4, 5).right_triangle())  # Проверка на прямоугольный треугольник
        # Проверка на Exception (если неверное соотношение сторон треугольника)
        print(Triangle(1, 2, 100).right_triangle())
    except TriangleException as e:
        print(e)


