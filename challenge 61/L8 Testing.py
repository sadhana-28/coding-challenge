import unittest

class TestLevel8Discounts(unittest.TestCase):

    # ✅ Positive case: senior citizen only
    def test_senior_discount(self):
        self.assertEqual(apply_discounts(4000, 65), 3600)

    # ✅ Positive case: high bill only
    def test_high_bill_discount(self):
        self.assertEqual(apply_discounts(6000, 40), 5700)

    # ✅ Positive case: senior + high bill
    def test_combined_discounts(self):
        self.assertEqual(apply_discounts(6000, 65), 5130)

    # ⚠️ Edge case: age exactly 60
    def test_age_boundary(self):
        self.assertEqual(apply_discounts(5000, 60), 4500)

    # ⚠️ Edge case: subtotal exactly 5000
    def test_subtotal_boundary(self):
        self.assertEqual(apply_discounts(5000, 30), 5000)

    # ❌ Negative case: invalid age
    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            apply_discounts(5000, -1)


if __name__ == "__main__":
    unittest.main()
