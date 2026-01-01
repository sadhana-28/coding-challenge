import unittest

class TestChallenge11(unittest.TestCase):

    #  Positive case
    def test_valid_salary(self):
        r = calculate_salary("John", "E12345", 70000, 15000, 10)
        self.assertEqual(r["Gross Monthly Salary"], 85000)

    #  Edge case
    def test_zero_bonus(self):
        r = calculate_salary("John", "E12345", 50000, 0, 0)
        self.assertEqual(r["Annual Gross Salary"], 600000)

    #  Negative case
    def test_negative_basic(self):
        with self.assertRaises(ValueError):
            calculate_salary("John", "E12345", -1000, 500, 10)

if __name__ == "__main__":
    unittest.main()
