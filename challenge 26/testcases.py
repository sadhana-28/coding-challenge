import unittest

# Import the function from your module
# Example:
# from challenge25 import calculate_item_total


class TestCalculateItemTotal(unittest.TestCase):
    """Unit tests for calculate_item_total function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_valid_item_details(self):
        result = calculate_item_total("ITM001", "Pen", 10, 15.0)

        self.assertEqual(result["Item Code"], "ITM001")
        self.assertEqual(result["Description"], "Pen")
        self.assertEqual(result["Quantity"], 10)
        self.assertEqual(result["Price per Unit"], 15.0)
        self.assertEqual(result["Total Cost"], 150.0)

    def test_single_quantity(self):
        result = calculate_item_total("ITM002", "Notebook", 1, 50.0)
        self.assertEqual(result["Total Cost"], 50.0)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_large_quantity_and_price(self):
        result = calculate_item_total("ITM003", "Printer", 1000, 25000.0)
        self.assertEqual(result["Total Cost"], 25_000_000.0)

    def test_float_price(self):
        result = calculate_item_total("ITM004", "Chocolate", 3, 19.99)
        self.assertAlmostEqual(result["Total Cost"], 59.97)

    # -------------------------
    # Negative Test Cases
    # -------------------------

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            calculate_item_total("ITM005", "Eraser", 0, 5.0)

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            calculate_item_total("ITM006", "Scale", -2, 20.0)

    def test_zero_price(self):
        with self.assertRaises(ValueError):
            calculate_item_total("ITM007", "Marker", 5, 0)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_item_total("ITM008", "Board", 5, -100.0)

    # -------------------------
    # Logical / Data Integrity Tests
    # -------------------------

    def test_item_code_and_description_preserved(self):
        result = calculate_item_total("ABC123", "Wireless Mouse", 2, 750.0)

        self.assertEqual(result["Item Code"], "ABC123")
        self.assertEqual(result["Description"], "Wireless Mouse")


if __name__ == "__main__":
    unittest.main()
