import unittest

class TestLevel4Subtotal(unittest.TestCase):

    # ✅ Positive case: multiple services
    def test_multiple_costs(self):
        self.assertEqual(calculate_subtotal([500, 1500]), 2000)

    # ⚠️ Edge case: no services selected
    def test_empty_costs(self):
        self.assertEqual(calculate_subtotal([]), 0)

    # ⚠️ Edge case: single service
    def test_single_cost(self):
        self.assertEqual(calculate_subtotal([500]), 500)

    # ❌ Negative case: non-numeric value
    def test_non_numeric_cost(self):
        with self.assertRaises(TypeError):
            calculate_subtotal([500, "1500"])


if __name__ == "__main__":
    unittest.main()
