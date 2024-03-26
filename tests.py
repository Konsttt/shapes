import unittest
from shapes import Circle, Triangle
from math import pi


class MyTestCase(unittest.TestCase):
    def test_circle_area(self):
        x = Circle(10).area() - pi * 10**2 < 0.0000001
        self.assertEqual(x, True)

    def test_triangle_area(self):
        self.assertEqual(Triangle(3, 4, 5).area(), 3*4/2)

    def test_right_triangle(self):
        self.assertEqual(Triangle(3, 4, 5).right_triangle(), True)

    def test_no_right_triangle(self):
        self.assertEqual(Triangle(5, 4, 5).right_triangle(), False)


if __name__ == '__main__':
    unittest.main()
