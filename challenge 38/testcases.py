import unittest
from io import StringIO
import sys

class TestStarIncreasing(unittest.TestCase):

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    def test_standard_pattern(self):
        print_star_increasing(4)
        self.assertEqual(
            sys.stdout.getvalue(),
            "*\n**\n***\n****\n"
        )

    def test_single_row(self):
        print_star_increasing(1)
        self.assertEqual(sys.stdout.getvalue(), "*\n")

    def test_zero_rows(self):
        print_star_increasing(0)
        self.assertEqual(sys.stdout.getvalue(), "")

if __name__ == "__main__":
    unittest.main()
