import unittest

# Import the functions from your module
# Example:
# from tax_calculator import (
#     calculate_annual_salary,
#     calculate_taxable_income,
#     calculate_tax_new_regime,
#     generate_tax_report,
#     STANDARD_DEDUCTION,
#     REBATE_LIMIT
# )

STANDARD_DEDUCTION = 50000
REBATE_LIMIT = 700000


class TestCalculateAnnualSalary(unittest.TestCase):
    """Test cases for calculate_annual_salary"""

    def test_valid_salary_components(self):
        monthly_components = {
            "Basic": 50000,
            "HRA": 20000,
            "Allowances": 10000
        }
        expected = (50000 + 20000 + 10000) * 12
        self.assertEqual(calculate_annual_salary(monthly_components), expected)

    def test_empty_salary_components(self):
        monthly_components = {}
        self.assertEqual(calculate_annual_salary(monthly_components), 0)

    def test_zero_salary_values(self):
        monthly_components = {"Basic": 0, "HRA": 0}
        self.assertEqual(calculate_annual_salary(monthly_components), 0)

    def test_negative_salary_value(self):
        monthly_components = {"Basic": -10000}
        with self.assertRaises(ValueError):
            calculate_annual_salary(monthly_components)

    def test_invalid_salary_structure(self):
        with self.assertRaises(ValueError):
            calculate_annual_salary(["Basic", 50000])


class TestCalculateTaxableIncome(unittest.TestCase):
    """Test cases for calculate_taxable_income"""

    def test_above_standard_deduction(self):
        gross_salary = 600000
        self.assertEqual(
            calculate_taxable_income(gross_salary),
            gross_salary - STANDARD_DEDUCTION
        )

    def test_exact_standard_deduction(self):
        self.assertEqual(calculate_taxable_income(50000), 0)

    def test_below_standard_deduction(self):
        self.assertEqual(calculate_taxable_income(30000), 0)

    def test_zero_gross_salary(self):
        self.assertEqual(calculate_taxable_income(0), 0)


class TestCalculateTaxNewRegime(unittest.TestCase):
    """Test cases for calculate_tax_new_regime"""

    def test_rebate_limit(self):
        self.assertEqual(calculate_tax_new_regime(REBATE_LIMIT), 0)

    def test_below_rebate_limit(self):_
