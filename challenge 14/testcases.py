import unittest

# Import the function and constant from your module
# Example:
# from challenge13 import calculate_tax, CESS_RATE

CESS_RATE = 0.04


class TestCalculateTax(unittest.TestCase):
    """Unit tests for calculate_tax function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_rebate_applicable(self):
        tax, cess, total = calculate_tax(700000)

        self.assertEqual(tax, 0)
        self.assertEqual(cess, 0)
        self.assertEqual(total, 0)

    def test_just_above_rebate_limit(self):
        tax, cess, total = calculate_tax(700001)

        self.assertGreater(tax, 0)
        self.assertAlmostEqual(cess, tax * CESS_RATE)
        self.assertAlmostEqual(total, tax + cess)

    def test_middle_slab_income(self):
        tax, cess, total = calculate_tax(970000)

        self.assertGreater(tax, 0)
        self.assertAlmostEqual(cess, tax * CESS_RATE)
        self.assertAlmostEqual(total, tax + cess)

    def test_highest_slab_income(self):
        tax, cess, total = calculate_tax(2000000)

        self.assertGreater(tax, 0)
        self.assertAlmostEqual(cess, tax * CESS_RATE)
        self.assertAlmostEqual(total, tax + cess)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_zero_taxable_income(self):
        tax, cess, total = calculate_tax(0)

        self.assertEqual(tax, 0)
        self.assertEqual(cess, 0)
        self.assertEqual(total, 0)

    def test_exact_first_slab_limit(self):
        tax, cess, total = calculate_tax(300000)

        self.assertEqual(tax, 0)
        self.assertEqual(cess, 0)
        self.assertEqual(total, 0)

    def test_exact_second_slab_limit(self):
        tax, cess, total = calculate_tax(600000)

        self.assertEqual(tax, 0)
        self.assertEqual(cess, 0)
        self.assertEqual(total, 0)

    def test_exact_third_slab_limit(self):
        tax, cess, total = calculate_tax(900000)

        self.assertGreaterEqual(tax, 0)
        self.assertAlmostEqual(cess, tax * CESS_RATE)
        self.assertAlmostEqual(total, tax + cess)

    def test_exact_upper_slab_limit(self):
        tax, cess, total = calculate_tax(1500000)

        self.assertGreaterEqual(tax, 0)
        self.assertAlmostEqual(cess, tax * CESS_RATE)
        self.assertAlmostEqual(total, tax + cess)

    # -------------------------
    # Data Type / Logical Tests
    # (No validation present in core logic)
    # -------------------------

    def test_float_taxable_income(self):
        tax, cess, total = calculate_tax(970000.50)

        self.assertAlmostEqual(cess, tax * CESS_RATE)
        self.assertAlmostEqual(total, tax + cess)

    def test_negative_taxable_income(self):
        tax, cess, total = calculate_tax(-50000)

        self.assertEqual(tax, 0)
        self.assertEqual(cess, 0)
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
