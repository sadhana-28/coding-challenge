import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge32 import check_minimum_purchase


class TestCheckMinimumPurchase(unittest.TestCase):
    """Unit tests for check_minimum_purchase function"""

    def setUp(self):
        """Redirect stdout before each test"""
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = self._stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_minimum_purchase_met(self):
        check_minimum_purchase(500)
        output = sys.stdout.getvalue()

        self.assertIn("Minimum purchase condition met", output)

    def test_above_minimum_purchase(self):
        check_minimum_purchase(1500)
        output = sys.stdout.getvalue()

        self.assertIn("Invoice generated", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_just_below_minimum_purchase(self):
        check_minimum_purchase(499)
        output = sys.stdout.getvalue()

        self.assertIn("Minimum purchase amount of ₹500 not met", output)

    def test_zero_total(self):
        check_minimum_purchase(0)
        output = sys.stdout.getvalue()

        self.assertIn("Minimum purchase amount of ₹500 not met", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_negative_total(self):
        check_minimum_purchase(-100)
        output = sys.stdout.getvalue()

        self.assertIn("Minimum purchase amount of ₹500 not met", output)


if __name__ == "__main__":
    unittest.main()
