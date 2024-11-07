import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertEqual(self.calc.add(10, 0), 10)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(9, 10), 90)
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(2, 4), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(4, 2), 0)
        self.assertEqual(self.calc.modulo(2, 4), 2)        

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()