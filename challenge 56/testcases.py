import unittest
from io import StringIO
import sys


class TestSum2DArray(unittest.TestCase):
    """Unit tests for summing elements of a 2D array"""

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_2x2_matrix(self):
        matrix = [[1, 2], [3, 4]]
        total = 0

        for row in matrix:
            for val in row:
                total += val

        print("Sum:", total)
        output = sys.stdout.getvalue()

        self.assertEqual(output, "Sum: 10\n")

    def test_single_row_matrix(self):
        matrix = [[5, 10, 15]]
        total = 0

        for row in matrix:
            for val in row:
                total += val

        print("Sum:", total)
        output = sys.stdout.getvalue()

        self.assertEqual(output, "Sum: 30\n")

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_single_element_matrix(self):
        matrix = [[7]]
        total = 0

        for row in matrix:
            for val in row:
                total += val

        print("Sum:", total)
        output = sys.stdout.getvalue()

        self.assertEqual(output, "Sum: 7\n")

    def test_empty_matrix(self):
        matrix = []
        total = 0

        for row in matrix:
            for val in row:
                total += val

        print("Sum:", total)
        output = sys.stdout.getvalue()

        self.assertEqual(output, "Sum: 0\n")

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_matrix_with_negative_values(self):
        matrix = [[-1, -2], [-3, -4]]
        total = 0

        for row in matrix:
            for val in row:
                total += val

        print("Sum:", total)
        output = sys.stdout.getvalue()

        self.assertEqual(output, "Sum: -10\n")

    def test_matrix_with_mixed_values(self):
        matrix = [[1, -2], [3, -4]]
        total = 0

        for row in matrix:
            for val in row:
                total += val

        print("Sum:", total)
        output = sys.stdout.getvalue()

        self.assertEqual(output, "Sum: -2\n")


if __name__ == "__main__":
    unittest.main()
