import unittest

# Import the function from your module
# Example:
# from challenge11 import calculate_salary


class TestCalculateSalary(unittest.TestCase):
    """Unit tests for calculate_salary function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_standard_salary_calculation(self):
        result = calculate_salary("John", "E12345", 70000, 15000, 10)

        self.assertEqual(result["Name"], "John")
        self.assertEqual(result["EmpID"], "E12345")
        self.assertEqual(result["Gross Monthly Salary"], 85000)
        self.assertEqual(result["Annual Gross Salary"], 1122000)

    def test_zero_bonus(self):
        result = calculate_salary("John", "E12345", 50000, 10000, 0)

        self.assertEqual(result["Gross Monthly Salary"], 60000)
        self.assertEqual(result["Annual Gross Salary"], 720000)

    def test_zero_special_allowance(self):
        result = calculate_salary("John", "E12345", 50000, 0, 10)

        self.assertEqual(result["Gross Monthly Salary"], 50000)
        self.assertEqual(result["Annual Gross Salary"], 660000)

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_basic_salary(self):
        result = calculate_salary("John", "E12345", 0, 10000, 10)

        self.assertEqual(result["Gross Monthly Salary"], 10000)
        self.assertEqual(result["Annual Gross Salary"], 132000)

    def test_zero_all_numeric_values(self):
        result = calculate_salary("John", "E12345", 0, 0, 0)

        self.assertEqual(result["Gross Monthly Salary"], 0)
        self.assertEqual(result["Annual Gross Salary"], 0)

    def test_high_bonus_percentage(self):
        result = calculate_salary("John", "E12345", 50000, 10000, 100)

        self.assertEqual(result["Gross Monthly Salary"], 60000)
        self.assertEqual(result["Annual Gross Salary"], 1440000)

    # -------------------------
    # Boundary / Data Type Tests
    # -------------------------

    def test_float_salary_values(self):
        result = calculate_salary("John", "E12345", 50000.50, 10000.25, 10)

        self.assertAlmostEqual(result["Gross Monthly Salary"], 60000.75)
        self.assertAlmostEqual(result["Annual Gross Salary"], 792009.9)

    def test_string_name_and_empid(self):
        result = calculate_salary("Alice", "EMP999", 40000, 5000, 5)

        self.assertEqual(result["Name"], "Alice")
        self.assertEqual(result["EmpID"], "EMP999")

    # -------------------------
    # Negative / Logical Tests
    # (Function allows these as no validation is present)
    # -------------------------

    def test_negative_salary_values(self):
        result = calculate_salary("John", "E12345", -50000, -10000, 10)

        self.assertEqual(result["Gross Monthly Salary"], -60000)
        self.assertEqual(result["Annual Gross Salary"], -792000)

    def test_negative_bonus_percentage(self):
        result = calculate_salary("John", "E12345", 50000, 10000, -10)

        self.assertEqual(result["Gross Monthly Salary"], 60000)
        self.assertEqual(result["Annual Gross Salary"], 648000)


if __name__ == "__main__":
    unittest.main()
