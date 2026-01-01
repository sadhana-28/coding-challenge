import unittest

# Import the function from your module
# Example:
# from challenge30 import calculate_item_total


class TestCalculateItemTotalPromo(unittest.TestCase):
    """Unit tests for calculate_item_total with promotional code logic"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_promo_code_applied(self):
        total = calculate_item_total("PROMO10", 500, 4)

        # 500 * 4 = 2000 → 10% discount → 1800
        self.assertEqual(total, 1800)

    def test_non_promo_code(self):
        total = calculate_item_total("ITEM01", 500, 4)

        # No discount applied
        self.assertEqual(total, 2000)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_zero_quantity(self):
        total = calculate_item_total("PROMO10", 500, 0)

        self.assertEqual(total, 0)

    def test_zero_price(self):
        total = calculate_item_total("PROMO10", 0, 5)

        self.assertEqual(total, 0)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_lowercase_promo_code(self):
        total = calculate_item_total("promo10", 500, 4)

        # Case-sensitive comparison, no discount
        self.assertEqual(total, 2000)

    def test_negative_price(self):
        total = calculate_item_total("PROMO10", -500, 2)

        # Function allows negative values as no validation is present
        self.assertEqual(total, -900)

    def test_negative_quantity(self):
        total = calculate_item_total("PROMO10", 500, -2)

        self.assertEqual(total, -900)


if __name__ == "__main__":
    unittest.main()
