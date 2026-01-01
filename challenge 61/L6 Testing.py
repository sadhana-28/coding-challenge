import unittest

class TestLevel6InvoiceTotal(unittest.TestCase):

    # ✅ Positive case
    def test_normal_invoice(self):
        self.assertAlmostEqual(calculate_grand_total(2000), 2360)

    # ⚠️ Edge case: zero bill
    def test_zero_invoice(self):
        self.assertEqual(calculate_grand_total(0), 0)

    # ⚠️ Edge case: large bill
    def test_large_invoice(self):
        self.assertAlmostEqual(calculate_grand_total(100000), 118000)


if __name__ == "__main__":
    unittest.main()
