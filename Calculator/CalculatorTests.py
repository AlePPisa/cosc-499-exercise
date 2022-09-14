import unittest
import Calculator


class CalculatorTests(unittest.TestCase):

    # Tests for addition functionality
    def test_addition(self):
        # Two positives
        self.assertEqual(2, Calculator.add(1, 1))

        # Two negatives
        self.assertEqual(-4, Calculator.add(-2, -2))

        # One of each
        self.assertEqual(-2, Calculator.add(-4, 2))

        # Two 0s
        self.assertEqual(0, Calculator.add(0, 0))

        # Exceptions
        with self.assertRaises(Exception):
            Calculator.add("a" + 9)


if __name__ == '__main__':
    unittest.main()
