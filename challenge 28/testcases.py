import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge27 import apply_discounts


class TestApplyDiscounts(unittest.TestCase):
    """Unit tests for apply_discounts function"""

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

    def test_both_discounts_applied(self):
        apply_discounts(12000, 25)
        output = sys.stdout.getvalue()

        # 12000 * 0.90 * 0.95 = 10260
        self.assertIn("₹10,260.00", output)

    def test_only_amount_discount_applied(self):
        apply_discounts(15000, 10)
        output = sys.stdout.getvalue()

        # 15000 * 0.90 = 13500
        self.assertIn("₹13,500.00", output)

    def test_only_quantity_discount_applied(self):
        apply_discounts(8000, 30)
        output = sys.stdout.getvalue()

        # 8000 * 0.95 = 7600
        self.assertIn("₹7,600.00", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_exact_grand_total_boundary(self):
        apply_discounts(10000, 10)
        output = sys.stdout.getvalue()

        # No discount applied
        self.assertIn("₹10,000.00", output)

    def test_exact_quantity_boundary(self):
        apply_discounts(8000, 20)
        output = sys.stdout.getvalue()

        # No quantity discount applied
        self.assertIn("₹8,000.00", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_zero_grand_total(self):
        apply_discounts(0, 50)
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    def test_negative_values(self):
        apply_discounts(-5000, -10)
        output = sys.stdout.getvalue()

        # No conditions met, value remains unchanged
        self.assertIn("₹-5,000.00", output)


if __name__ == "__main__":
    unittest.main()
