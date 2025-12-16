import unittest

# Import the function from your module
# Example:
# from challenge14 import calculate_net_salary


class TestCalculateNetSalary(unittest.TestCase):
    """Unit tests for calculate_net_salary function"""

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_normal_net_salary(self):
        net_salary = calculate_net_salary(1020000, 76800)
        self.assertEqual(net_salary, 943200)

    def test_zero_tax(self):
        net_salary = calculate_net_salary(500000, 0)
        self.assertEqual(net_salary, 500000)

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_zero_annual_salary(self):
        net_salary = calculate_net_salary(0, 0)
        self.assertEqual(net_salary, 0)

    def test_tax_equals_salary(self):
        net_salary = calculate_net_salary(100000, 100000)
        self.assertEqual(net_salary, 0)

    # -------------------------
    # Boundary / Data Type Tests
    # -------------------------

    def test_float_values(self):
        net_salary = calculate_net_salary(1020000.50, 76800.25)
        self.assertAlmostEqual(net_salary, 943200.25)

    # -------------------------
    # Negative / Logical Tests
    # (Function allows these as no validation is present)
    # -------------------------

    def test_tax_greater_than_salary(self):
        net_salary = calculate_net_salary(100000, 150000)
        self.assertEqual(net_salary, -50000)

    def test_negative_tax_value(self):
        net_salary = calculate_net_salary(100000, -5000)
        self.assertEqual(net_salary, 105000)


if __name__ == "__main__":
    unittest.main()
