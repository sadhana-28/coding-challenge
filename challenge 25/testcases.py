import unittest

# Import the function from your module
# Example:
# from challenge25 import generate_invoice


class TestGenerateInvoice(unittest.TestCase):
    """Unit tests for generate_invoice function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_invoice(self):
        items = [
            {"name": "ItemA", "price": 1000, "quantity": 2},
            {"name": "ItemB", "price": 500, "quantity": 3}
        ]

        bill = generate_invoice(items)

        self.assertEqual(bill["subtotal"], 3500)
        self.assertEqual(bill["discount"], 0)
        self.assertEqual(bill["surcharge"], 0)
        self.assertAlmostEqual(bill["gst"], 175)
        self.assertAlmostEqual(bill["total"], 3675)

    def test_discount_5_percent(self):
        items = [
            {"name": "ItemA", "price": 1000, "quantity": 5}
        ]

        bill = generate_invoice(items)

        self.assertEqual(bill["subtotal"], 5000)
        self.assertEqual(bill["discount"], 250)
        self.assertEqual(bill["surcharge"], 0)

    def test_discount_10_percent(self):
        items = [
            {"name": "ItemA", "price": 2000, "quantity": 5}
        ]

        bill = generate_invoice(items)

        self.assertEqual(bill["subtotal"], 10000)
        self.assertEqual(bill["discount"], 1000)

    def test_quantity_surcharge_applied(self):
        items = [
            {"name": "BulkItem", "price": 100, "quantity": 11}
        ]

        bill = generate_invoice(items)

        self.assertEqual(bill["subtotal"], 1100)
        self.assertAlmostEqual(bill["surcharge"], 22)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_exact_quantity_boundary(self):
        items = [
            {"name": "ItemA", "price": 100, "quantity": 10}
        ]

        bill = generate_invoice(items)

        self.assertEqual(bill["surcharge"], 0)

    def test_empty_items_list(self):
        bill = generate_invoice([])

        self.assertEqual(bill["subtotal"], 0)
        self.assertEqual(bill["discount"], 0)
        self.assertEqual(bill["surcharge"], 0)
        self.assertEqual(bill["gst"], 0)
        self.assertEqual(bill["total"], 0)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_multiple_items_surcharge_applied_once(self):
        items = [
            {"name": "ItemA", "price": 100, "quantity": 12},
            {"name": "ItemB", "price": 200, "quantity": 1}
        ]

        bill = generate_invoice(items)

        self.assertAlmostEqual(bill["surcharge"], bill["subtotal"] * 0.02)


if __name__ == "__main__":
    unittest.main()
