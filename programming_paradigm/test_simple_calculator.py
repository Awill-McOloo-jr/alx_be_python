import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative + positive
        self.assertEqual(self.calc.add(-2, -3), -5)  # Negative + negative
        self.assertEqual(self.calc.add(0, 0), 0)  # Zero + zero

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(3, 5), -2)  # Subtracting larger from smaller
        self.assertEqual(self.calc.subtract(-5, -3), -2)  # Negative - negative
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Zero - zero

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Negative * positive
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Negative * negative
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Zero * any number
        self.assertEqual(self.calc.multiply(0, 0), 0)  # Zero * zero

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Normal division
        self.assertEqual(self.calc.divide(-6, 3), -2)  # Negative / positive
        self.assertEqual(self.calc.divide(6, -3), -2)  # Positive / negative
        self.assertEqual(self.calc.divide(-6, -3), 2)  # Negative / negative
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Division resulting in float

        # Test division by zero
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero should return None
        self.assertEqual(self.calc.divide(0, 0), None)  # Zero divided by zero should also return None
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero divided by any number is 0

if __name__ == "__main__":
    unittest.main()
