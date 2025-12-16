import unittest

# Import the function from your module
# Example:
# from challenge16 import validate_inputs


class TestValidateInputs(unittest.TestCase):
    """Unit tests for validate_inputs function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_all_valid_inputs(self):
        result = validate_inputs("John", "E12345", 70000, 15000, 10)
        self.assertTrue(result)

    def test_valid_min_empid_length(self):
        result = validate_inputs("Alice", "A1234", 50000, 0, 0)
        self.assertTrue(result)

    def test_valid_max_empid_length(self):
        result = validate_inputs("Alice", "EMPID12345", 50000, 1000, 100)
        self.assertTrue(result)

    # -------------------------
    # Edge / Boundary Test Cases
    # -------------------------

    def test_bonus_lower_boundary(self):
        result = validate_inputs("Mark", "M12345", 40000, 5000, 0)
        self.assertTrue(result)

    def test_bonus_upper_boundary(self):
        result = validate_inputs("Mark", "M12345", 40000, 5000, 100)
        self.assertTrue(result)

    def test_zero_allowance(self):
        result = validate_inputs("Ravi", "R12345", 30000, 0, 20)
        self.assertTrue(result)

    # -------------------------
    # Negative Test Cases
    # -------------------------

    def test_name_with_numbers(self):
        with self.assertRaises(ValueError):
            validate_inputs("John123", "E12345", 70000, 15000, 10)

    def test_name_with_special_characters(self):
        with self.assertRaises(ValueError):
            validate_inputs("John@", "E12345", 70000, 15000, 10)

    def test_invalid_empid_non_alphanumeric(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E12@45", 70000, 15000, 10)

    def test_empid_too_short(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E123", 70000, 15000, 10)

    def test_empid_too_long(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "EMPID1234567", 70000, 15000, 10)

    def test_basic_salary_zero(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E12345", 0, 15000, 10)

    def test_basic_salary_negative(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E12345", -50000, 15000, 10)

    def test_negative_allowance(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E12345", 50000, -1000, 10)

    def test_bonus_below_zero(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E12345", 50000, 1000, -1)

    def test_bonus_above_hundred(self):
        with self.assertRaises(ValueError):
            validate_inputs("John", "E12345", 50000, 1000, 101)


if __name__ == "__main__":
    unittest.main()
