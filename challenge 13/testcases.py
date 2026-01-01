import unittest

# Import the function from your module
# Example:
# from challenge12 import calculate_taxable_income, STANDARD_DEDUCTION


STANDARD_DEDUCTION = 50000


class TestCalculateTaxableIncome(unittest.TestCase):
    """Unit tests for calculate_taxable_income function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_normal_annual_salary(self):
        gross, deduction, taxable = calculate_taxable_income(1020000)

        self.assertEqual(gross, 1020000)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 970000)

    def test_salary_just_above_deduction(self):
        gross, deduction, taxable = calculate_taxable_income(50001)

        self.assertEqual(gross, 50001)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 1)

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_salary_equal_to_deduction(self):
        gross, deduction, taxable = calculate_taxable_income(50000)

        self.assertEqual(gross, 50000)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 0)

    def test_salary_below_deduction(self):
        gross, deduction, taxable = calculate_taxable_income(30000)

        self.assertEqual(gross, 30000)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 0)

    def test_zero_salary(self):
        gross, deduction, taxable = calculate_taxable_income(0)

        self.assertEqual(gross, 0)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 0)

    # -------------------------
    # Boundary / Data Type Tests
    # -------------------------

    def test_float_salary_value(self):
        gross, deduction, taxable = calculate_taxable_income(1020000.50)

        self.assertEqual(gross, 1020000.50)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 970000.50)

    def test_large_salary_value(self):
        gross, deduction, taxable = calculate_taxable_income(10_000_000)

        self.assertEqual(gross, 10_000_000)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 9_950_000)

    # -------------------------
    # Negative / Logical Tests
    # (Function allows these as no validation is present)
    # -------------------------

    def test_negative_salary(self):
        gross, deduction, taxable = calculate_taxable_income(-100000)

        self.assertEqual(gross, -100000)
        self.assertEqual(deduction, STANDARD_DEDUCTION)
        self.assertEqual(taxable, 0)


if __name__ == "__main__":
    unittest.main()
