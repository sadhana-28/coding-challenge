import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge29 import calculate_tax


class TestCalculateTax(unittest.TestCase):
    """Unit tests for calculate_tax function"""

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

    def test_tax_below_5000(self):
        calculate_tax(4000)
        output = sys.stdout.getvalue()

        # Tax = 5% of 4000 = 200
        self.assertIn("₹200.00", output)
        self.assertIn("₹4,200.00", output)

    def test_tax_between_5000_and_20000(self):
        calculate_tax(18000)
        output = sys.stdout.getvalue()

        # Tax = 10% of 18000 = 1800
        self.assertIn("₹1,800.00", output)
        self.assertIn("₹19,800.00", output)

    def test_tax_above_20000(self):
        calculate_tax(25000)
        output = sys.stdout.getvalue()

        # Tax = 15% of 25000 = 3750
        self.assertIn("₹3,750.00", output)
        self.assertIn("₹28,750.00", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_exact_5000(self):
        calculate_tax(5000)
        output = sys.stdout.getvalue()

        # 10% slab applies
        self.assertIn("₹500.00", output)
        self.assertIn("₹5,500.00", output)

    def test_exact_20000(self):
        calculate_tax(20000)
        output = sys.stdout.getvalue()

        # 10% slab applies
        self.assertIn("₹2,000.00", output)
        self.assertIn("₹22,000.00", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_zero_total(self):
        calculate_tax(0)
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    def test_negative_total(self):
        calculate_tax(-1000)
        output = sys.stdout.getvalue()

        # Tax = -5% of -1000 = -50
        self.assertIn("₹-50.00", output)
        self.assertIn("₹-1,050.00", output)


if __name__ == "__main__":
    unittest.main()
