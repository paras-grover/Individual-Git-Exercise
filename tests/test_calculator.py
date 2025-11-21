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


if __name__ == "__main__":
    unittest.main()
