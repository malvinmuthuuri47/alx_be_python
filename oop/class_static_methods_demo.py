"""
This module intends to showcase OOP static and class methods
"""

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @classmethod
    def multiply(cls, a: int, b: int) -> int:
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
