"""
This module defines OOP concepts Polymorphism and Method overloading
"""

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must define this method")

class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi ** self.radius
