import unittest
from io import StringIO
import sys

class TestFixedNumberPattern(unittest.TestCase):

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    def test_standard_pattern(self):
        print_fixed_number_pattern(4)
        self.assertEqual(
            sys.stdout.getvalue(),
            "1234\n1234\n1234\n1234\n"
        )

    def test_single_row(self):
        print_fixed_number_pattern(1)
        self.assertEqual(sys.stdout.getvalue(), "1\n")

    def test_zero_rows(self):
        print_fixed_number_pattern(0)
        self.assertEqual(sys.stdout.getvalue(), "")

if __name__ == "__main__":
    unittest.main()
