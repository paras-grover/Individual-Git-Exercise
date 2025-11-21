import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_valid_numbers(self):
        """Test addition with a valid space-separated string"""
        result = self.calc.add("1 2 3 4")
        self.assertEqual(result, 10)

    def test_add_invalid_input(self):
        """Test that method handles non-integer values correctly"""
        result = self.calc.add("1 two 3")
        self.assertEqual(result, "Please enter valid integers with spaces in between")
    
    def test_division_valid(self):
        """Test normal division"""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        """Test divide-by-zero error message"""
        result = self.calc.divide(10, 0)
        self.assertEqual(result, "Denominator cannot be 0")


if __name__ == "__main__":
    unittest.main()
