import unittest
from io import StringIO
import sys


class TestMatrixTranspose(unittest.TestCase):
    """Unit tests for matrix transpose logic"""

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_matrix_transpose(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        rows = len(matrix)
        cols = len(matrix[0])

        transpose = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]

        print("Matrix:")
        for row in matrix:
            print(row)

        print("Transpose:")
        for row in transpose:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Matrix:\n"
            "[1, 2, 3]\n"
            "[4, 5, 6]\n"
            "Transpose:\n"
            "[1, 4]\n"
            "[2, 5]\n"
            "[3, 6]\n"
        )

        self.assertEqual(output, expected_output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_single_row_matrix(self):
        matrix = [[10, 20, 30]]
        rows = len(matrix)
        cols = len(matrix[0])

        transpose = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]

        print("Matrix:")
        for row in matrix:
            print(row)

        print("Transpose:")
        for row in transpose:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Matrix:\n"
            "[10, 20, 30]\n"
            "Transpose:\n"
            "[10]\n"
            "[20]\n"
            "[30]\n"
        )

        self.assertEqual(output, expected_output)

    def test_single_column_matrix(self):
        matrix = [[1], [2], [3]]
        rows = len(matrix)
        cols = len(matrix[0])

        transpose = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]

        print("Matrix:")
        for row in matrix:
            print(row)

        print("Transpose:")
        for row in transpose:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Matrix:\n"
            "[1]\n"
            "[2]\n"
            "[3]\n"
            "Transpose:\n"
            "[1, 2, 3]\n"
        )

        self.assertEqual(output, expected_output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_matrix_with_negative_values(self):
        matrix = [[-1, -2], [-3, -4]]
        rows = len(matrix)
        cols = len(matrix[0])

        transpose = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transpose[j][i] = matrix[i][j]

        print("Matrix:")
        for row in matrix:
            print(row)

        print("Transpose:")
        for row in transpose:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Matrix:\n"
            "[-1, -2]\n"
            "[-3, -4]\n"
            "Transpose:\n"
            "[-1, -3]\n"
            "[-2, -4]\n"
        )

        self.assertEqual(output, expected_output)

    # -------------------------
    # Error Behavior Test
    # -------------------------

    def test_empty_matrix_raises_error(self):
        matrix = []

        with self.assertRaises(IndexError):
            rows = len(matrix)
            cols = len(matrix[0])


if __name__ == "__main__":
    unittest.main()
