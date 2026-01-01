import unittest
from io import StringIO
import sys

# Import the function from your module
# Example:
# from challenge15 import generate_report


class TestGenerateReport(unittest.TestCase):
    """Unit tests for generate_report function"""

    def setUp(self):
        """Redirect stdout before each test"""
        self.held_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Restore stdout after each test"""
        sys.stdout = self.held_stdout

    # -------------------------
    # Positive Test Cases
    # -------------------------

    def test_valid_report_output(self):
        details = {
            "Name": "John Doe",
            "EmpID": "E12345",
            "Annual Gross Salary": 1020000,
            "Tax Payable": 76800
        }

        generate_report(details)
        output = sys.stdout.getvalue()

        self.assertIn("Employee Tax Report", output)
        self.assertIn("Name", output)
        self.assertIn("John Doe", output)
        self.assertIn("Annual Gross Salary", output)
        self.assertIn("₹1,020,000.00", output)
        self.assertIn("Tax Payable", output)
        self.assertIn("₹76,800.00", output)

    # -------------------------
    # Edge Test Cases
    # -------------------------

    def test_empty_details_dictionary(self):
        details = {}

        generate_report(details)
        output = sys.stdout.getvalue()

        self.assertIn("Employee Tax Report", output)
        self.assertNotIn("₹", output)

    def test_zero_numeric_values(self):
        details = {
            "Gross Salary": 0,
            "Tax": 0
        }

        generate_report(details)
        output = sys.stdout.getvalue()

        self.assertIn("₹0.00", output)

    # -------------------------
    # Boundary / Data Type Tests
    # -------------------------

    def test_float_values_formatting(self):
        details = {
            "Net Salary": 943200.50
        }

        generate_report(details)
        output = sys.stdout.getvalue()

        self.assertIn("₹943,200.50", output)

    def test_non_numeric_values(self):
        details = {
            "Department": "Finance"
        }

        generate_report(details)
        output = sys.stdout.getvalue()

        self.assertIn("Department", output)
        self.assertIn("Finance", output)

    # -------------------------
    # Logical Behavior Tests
    # -------------------------

    def test_preserves_all_keys(self):
        details = {
            "A": 1,
            "B": "Text",
            "C": 2.5
        }

        generate_report(details)
        output = sys.stdout.getvalue()

        self.assertIn("A", output)
        self.assertIn("B", output)
        self.assertIn("C", output)


if __name__ == "__main__":
    unittest.main()
