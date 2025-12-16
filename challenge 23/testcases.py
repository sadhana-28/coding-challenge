import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge23 import series_23


class TestSeries23(unittest.TestCase):
    """Unit tests for series_23 function"""

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

    def test_standard_series(self):
        series_23(5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 4 7 12 23")

    def test_single_element(self):
        series_23(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1")

    def test_two_elements(self):
        series_23(2)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 4")

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_input(self):
        series_23(0)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_negative_input(self):
        series_23(-5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    # -------------------------
    # Boundary / Logical Tests
    # -------------------------

    def test_beyond_defined_differences(self):
        series_23(7)
        output = sys.stdout.getvalue().strip()
        # differences used: 3, 3, 5, 11, 11, 11
        self.assertEqual(output, "1 4 7 12 23 34 45")


if __name__ == "__main__":
    unittest.main()
