"""
Тесты для простого калькулятора
"""

import unittest
from calculator import add, subtract, multiply, divide, calculate

class TestCalculator(unittest.TestCase):
    """Тесты для функций калькулятора"""
    
    def test_add(self):
        """Тест сложения"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -3), -8)
    
    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-1, -1), 0)
    
    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
    
    def test_divide(self):
        """Тест деления"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertEqual(divide(-10, 2), -5)
        
    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_calculate_add(self):
        """Тест функции calculate для сложения"""
        self.assertEqual(calculate(5, '+', 3), 8)
    
    def test_calculate_subtract(self):
        """Тест функции calculate для вычитания"""
        self.assertEqual(calculate(10, '-', 4), 6)
    
    def test_calculate_multiply(self):
        """Тест функции calculate для умножения"""
        self.assertEqual(calculate(6, '*', 7), 42)
    
    def test_calculate_divide(self):
        """Тест функции calculate для деления"""
        self.assertEqual(calculate(20, '/', 4), 5)
    
    def test_calculate_invalid_operator(self):
        """Тест неподдерживаемой операции"""
        with self.assertRaises(ValueError):
            calculate(5, '%', 2)
    
    def test_calculate_float_numbers(self):
        """Тест с дробными числами"""
        self.assertAlmostEqual(calculate(5.5, '+', 2.5), 8.0)
        self.assertAlmostEqual(calculate(10.0, '/', 4.0), 2.5)

if __name__ == '__main__':
    unittest.main()
