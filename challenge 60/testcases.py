import unittest
from io import StringIO
import sys


class TestMatrixMultiplication(unittest.TestCase):
    """Unit tests for matrix multiplication logic"""

    def setUp(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self._stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_2x2_matrix_multiplication(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]

        result = [[0, 0], [0, 0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        print("Resultant Matrix:")
        for row in result:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Resultant Matrix:\n"
            "[19, 22]\n"
            "[43, 50]\n"
        )

        self.assertEqual(output, expected_output)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_identity_matrix_multiplication(self):
        A = [[1, 0], [0, 1]]
        B = [[9, 8], [7, 6]]

        result = [[0, 0], [0, 0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        print("Resultant Matrix:")
        for row in result:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Resultant Matrix:\n"
            "[9, 8]\n"
            "[7, 6]\n"
        )

        self.assertEqual(output, expected_output)

    def test_zero_matrix_multiplication(self):
        A = [[0, 0], [0, 0]]
        B = [[5, 6], [7, 8]]

        result = [[0, 0], [0, 0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        print("Resultant Matrix:")
        for row in result:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Resultant Matrix:\n"
            "[0, 0]\n"
            "[0, 0]\n"
        )

        self.assertEqual(output, expected_output)

    # -------------------------
    # Logical / Data Tests
    # -------------------------

    def test_matrix_with_negative_values(self):
        A = [[-1, 2], [3, -4]]
        B = [[5, -6], [-7, 8]]

        result = [[0, 0], [0, 0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]

        print("Resultant Matrix:")
        for row in result:
            print(row)

        output = sys.stdout.getvalue()

        expected_output = (
            "Resultant Matrix:\n"
            "[-19, 22]\n"
            "[43, -50]\n"
        )

        self.assertEqual(output, expected_output)

    # -------------------------
    # Error Behavior Test
    # -------------------------

    def test_dimension_mismatch_raises_error(self):
        A = [[1, 2, 3]]
        B = [[1, 2], [3, 4]]

        with self.assertRaises(IndexError):
            result = [[0, 0]]

            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        result[i][j] += A[i][k] * B[k][j]


if __name__ == "__main__":
    unittest.main()
