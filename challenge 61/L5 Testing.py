import unittest

class TestLevel5GST(unittest.TestCase):

    # ✅ Positive case: normal subtotal
    def test_valid_subtotal(self):
        self.assertAlmostEqual(apply_gst(2000), 360.0)

    # ⚠️ Edge case: zero subtotal
    def test_zero_subtotal(self):
        self.assertEqual(apply_gst(0), 0)

    # ⚠️ Edge case: very large subtotal
    def test_large_subtotal(self):
        self.assertAlmostEqual(apply_gst(1_000_000), 180000)

    # ❌ Negative case: negative subtotal
    def test_negative_subtotal(self):
        with self.assertRaises(ValueError):
            apply_gst(-1000)


if __name__ == "__main__":
    unittest.main()
