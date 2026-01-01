import unittest
from io import StringIO
import sys

class TestNumberTriangle(unittest.TestCase):

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    def test_standard_pattern(self):
        print_number_triangle(4)
        self.assertEqual(
            sys.stdout.getvalue(),
            "1\n12\n123\n1234\n"
        )

    def test_single_row(self):
        print_number_triangle(1)
        self.assertEqual(sys.stdout.getvalue(), "1\n")

    def test_zero_rows(self):
        print_number_triangle(0)
        self.assertEqual(sys.stdout.getvalue(), "")

    def test_negative_rows(self):
        print_number_triangle(-3)
        self.assertEqual(sys.stdout.getvalue(), "")

if __name__ == "__main__":
    unittest.main()
