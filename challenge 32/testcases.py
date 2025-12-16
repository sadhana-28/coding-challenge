import unittest
from unittest.mock import patch
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge31 import apply_payment_surcharge


class TestApplyPaymentSurcharge(unittest.TestCase):
    """Unit tests for apply_payment_surcharge function"""

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

    @patch("builtins.input", return_value="card")
    def test_card_payment_applies_surcharge(self, mock_input):
        apply_payment_surcharge(12000)
        output = sys.stdout.getvalue()

        # Surcharge = 2% of 12000 = 240
        self.assertIn("₹240.00", output)
        self.assertIn("₹12,240.00", output)

    @patch("builtins.input", return_value="cash")
    def test_cash_payment_no_surcharge(self, mock_input):
        apply_payment_surcharge(12000)
        output = sys.stdout.getvalue()

        self.assertNotIn("Card Surcharge", output)
        self.assertIn("₹12,000.00", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    @patch("builtins.input", return_value="CARD")
    def test_uppercase_card_input(self, mock_input):
        apply_payment_surcharge(5000)
        output = sys.stdout.getvalue()

        # .lower() converts "CARD" to "card"
        self.assertIn("₹100.00", output)
        self.assertIn("₹5,100.00", output)

    @patch("builtins.input", return_value="")
    def test_empty_input(self, mock_input):
        apply_payment_surcharge(5000)
        output = sys.stdout.getvalue()

        # No surcharge applied
        self.assertIn("₹5,000.00", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    @patch("builtins.input", return_value="card")
    def test_zero_total(self, mock_input):
        apply_payment_surcharge(0)
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    @patch("builtins.input", return_value="card")
    def test_negative_total(self, mock_input):
        apply_payment_surcharge(-1000)
        output = sys.stdout.getvalue()

        # Surcharge = -20, final = -1020
        self.assertIn("₹-20.00", output)
        self.assertIn("₹-1,020.00", output)


if __name__ == "__main__":
    unittest.main()
