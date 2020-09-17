from calculator import Calculator
import unittest
from unittest import mock

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_no_add_calls_1(self):
        lastSum = self.calc.sum()
        self.assertEqual(0, lastSum)
    
    def test_sum_no_add_calls_2(self):
        self.calc.add(1)
        lastSum = self.calc.sum()
        self.assertEqual(1, lastSum)
    

if __name__ == "__main__":
    unittest.main()