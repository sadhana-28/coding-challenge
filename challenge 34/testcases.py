import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge33 import calculate_loyalty_points


class TestCalculateLoyaltyPoints(unittest.TestCase):
    """Unit tests for calculate_loyalty_points function"""

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

    def test_standard_loyalty_points(self):
        calculate_loyalty_points(9432)
        output = sys.stdout.getvalue()

        # 9432 // 100 = 94
        self.assertIn("Loyalty Points Earned: 94", output)

    def test_exact_multiple_of_100(self):
        calculate_loyalty_points(5000)
        output = sys.stdout.getvalue()

        self.assertIn("Loyalty Points Earned: 50", output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_just_below_100(self):
        calculate_loyalty_points(99)
        output = sys.stdout.getvalue()

        self.assertIn("Loyalty Points Earned: 0", output)

    def test_exact_100(self):
        calculate_loyalty_points(100)
        output = sys.stdout.getvalue()

        self.assertIn("Loyalty Points Earned: 1", output)

    def test_zero_total(self):
        calculate_loyalty_points(0)
        output = sys.stdout.getvalue()

        self.assertIn("Loyalty Points Earned: 0", output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_float_total(self):
        calculate_loyalty_points(1234.56)
        output = sys.stdout.getvalue()

        # 1234.56 // 100 = 12.0 -> int(12.0) = 12
        self.assertIn("Loyalty Points Earned: 12", output)

    def test_negative_total(self):
        calculate_loyalty_points(-500)
        output = sys.stdout.getvalue()

        # -500 // 100 = -5
        self.assertIn("Loyalty Points Earned: -5", output)


if __name__ == "__main__":
    unittest.main()
