import unittest

# Import the function from your module
# Example:
# from challenge44 import reverse_number


class TestReverseNumber(unittest.TestCase):
    """Unit tests for reverse_number function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_number(self):
        self.assertEqual(reverse_number(12345), 54321)

    def test_single_digit(self):
        self.assertEqual(reverse_number(7), 7)

    def test_number_with_zeros(self):
        self.assertEqual(reverse_number(1200), 21)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_zero(self):
        self.assertEqual(reverse_number(0), 0)

    def test_large_number(self):
        self.assertEqual(reverse_number(987654321), 123456789)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_negative_number(self):
        # While loop condition (num > 0) fails immediately
        # Function returns initial reverse = 0
        self.assertEqual(reverse_number(-123), 0)

    def test_trailing_zeroes(self):
        self.assertEqual(reverse_number(1000), 1)


if __name__ == "__main__":
    unittest.main()
