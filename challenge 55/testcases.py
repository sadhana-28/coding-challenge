import unittest
from io import StringIO
import sys


class TestDisplay2DArray(unittest.TestCase):
    """Unit tests for displaying 2D array row-wise"""

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

        for row in matrix:
            for element in row:
                print(element, end=" ")
            print()

        output = sys.stdout.getvalue()

        expected_output = "1 2 \n3 4 \n"
        self.assertEqual(output, expected_output)

    def test_single_row_matrix(self):
        matrix = [[10, 20, 30]]

        for row in matrix:
            for element in row:
                print(element, end=" ")
            print()

        output = sys.stdout.getvalue()

        self.assertEqual(output, "10 20 30 \n")

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_single_element_matrix(self):
        matrix = [[5]]

        for row in matrix:
            for element in row:
                print(element, end=" ")
            print()

        output = sys.stdout.getvalue()

        self.assertEqual(output, "5 \n")

    def test_empty_matrix(self):
        matrix = []

        for row in matrix:
            for element in row:
                print(element, end=" ")
            print()

        output = sys.stdout.getvalue()

        self.assertEqual(output, "")

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_matrix_with_negative_numbers(self):
        matrix = [[-1, -2], [-3, -4]]

        for row in matrix:
            for element in row:
                print(element, end=" ")
            print()

        output = sys.stdout.getvalue()

        expected_output = "-1 -2 \n-3 -4 \n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
