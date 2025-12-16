import unittest
from io import StringIO
import sys

class TestStarPattern(unittest.TestCase):

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    def test_standard_pattern(self):
        print_star_pattern(4)
        self.assertEqual(sys.stdout.getvalue(), "****\n****\n****\n****\n")

    def test_single_row(self):
        print_star_pattern(1)
        self.assertEqual(sys.stdout.getvalue(), "*\n")

    def test_zero_rows(self):
        print_star_pattern(0)
        self.assertEqual(sys.stdout.getvalue(), "")

    def test_negative_rows(self):
        print_star_pattern(-3)
        self.assertEqual(sys.stdout.getvalue(), "")

if __name__ == "__main__":
    unittest.main()
