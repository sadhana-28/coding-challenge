import unittest
from io import StringIO
import sys

class TestSquareAlternatePattern(unittest.TestCase):

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    def test_standard_pattern(self):
        print_square_alternate_pattern(4)
        self.assertEqual(
            sys.stdout.getvalue(),
            "1 \n-4 9 \n-16 25 -36 \n49 -64 81 -100 \n"
        )

    def test_single_row(self):
        print_square_alternate_pattern(1)
        self.assertEqual(sys.stdout.getvalue(), "1 \n")

    def test_zero_rows(self):
        print_square_alternate_pattern(0)
        self.assertEqual(sys.stdout.getvalue(), "")

if __name__ == "__main__":
    unittest.main()
