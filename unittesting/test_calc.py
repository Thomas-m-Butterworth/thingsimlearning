# This file will be used to test calc functions
import unittest
import calc

# Create test cases
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)   # Edge Case
        self.assertEqual(calc.add(-1, -1), -2)  # Edge Case

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)   # Edge Case
        self.assertEqual(calc.subtract(-1, -1), 0)   # Edge Case

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)   # Edge Case
        self.assertEqual(calc.multiply(-1, -1), 1)  # Edge Case

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)   # Edge Case
        self.assertEqual(calc.divide(-1, -1), 1)  # Edge Case
        self.assertEqual(calc.divide(5, 2), 2.5)    # Edge Case to account for floor division
        with self.assertRaises(ValueError):   # Tests for proper ValueError. Context manager.
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
