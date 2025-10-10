import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a new SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---------- Addition Tests ----------
    def test_addition_with_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_with_negative_numbers(self):
        """Test addition with negative operands."""
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_with_mixed_signs(self):
        """Test addition where operands have opposite signs."""
        self.assertEqual(self.calc.add(-5, 10), 5)

    def test_addition_with_zero(self):
        """Test addition when one operand is zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

    # ---------- Subtraction Tests ----------
    def test_subtraction_with_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_with_negative_numbers(self):
        """Test subtraction with negative operands."""
        self.assertEqual(self.calc.subtract(-5, -2), -3)

    def test_subtraction_with_mixed_signs(self):
        """Test subtraction where operands have opposite signs."""
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtraction_with_zero(self):
        """Test subtraction when one operand is zero."""
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # ---------- Multiplication Tests ----------
    def test_multiplication_with_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiplication_with_negative_numbers(self):
        """Test multiplication with negative operands."""
        self.assertEqual(self.calc.multiply(-4, -5), 20)

    def test_multiplication_with_mixed_signs(self):
        """Test multiplication where operands have opposite signs."""
        self.assertEqual(self.calc.multiply(-4, 5), -20)

    def test_multiplication_with_zero(self):
        """Test multiplication when one operand is zero."""
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    # ---------- Division Tests ----------
    def test_division_with_positive_numbers(self):
        """Test division of two positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_with_negative_numbers(self):
        """Test division with negative operands."""
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_with_mixed_signs(self):
        """Test division where operands have opposite signs."""
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))

    def test_division_zero_numerator(self):
        """Test division when numerator is zero."""
        self.assertEqual(self.calc.divide(0, 5), 0)

    def test_division_result_is_float(self):
        """Test division returns a float value for non-integer results."""
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)

if __name__ == "__main__":
    unittest.main()
