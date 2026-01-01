import unittest

class TestPatientDetails(unittest.TestCase):

    # =========================
    # ✅ POSITIVE TEST CASES
    # =========================

    def test_valid_male_patient(self):
        data = store_patient_details("Arjun Kumar", 35, "Male", "9876543210")
        self.assertEqual(data["gender"], "Male")

    def test_valid_female_patient(self):
        data = store_patient_details("Ananya", 28, "Female", "9123456789")
        self.assertEqual(data["gender"], "Female")

    def test_gender_case_insensitive(self):
        data = store_patient_details("Riya", 22, "fEmAlE", "9000000001")
        self.assertEqual(data["gender"], "Female")

    def test_name_with_spaces(self):
        data = store_patient_details("  Ravi  ", 40, "Male", "9999999999")
        self.assertEqual(data["name"], "Ravi")

    # =========================
    # ⚠️ EDGE CASES
    # =========================

    def test_age_zero(self):
        data = store_patient_details("Newborn", 0, "Female", "9000000002")
        self.assertEqual(data["age"], 0)

    def test_age_upper_boundary(self):
        data = store_patient_details("Senior", 120, "Male", "9000000003")
        self.assertEqual(data["age"], 120)

    def test_name_length_boundary(self):
        name = "A" * 50
        data = store_patient_details(name, 30, "Male", "9000000004")
        self.assertEqual(len(data["name"]), 50)

    # =========================
    # ❌ NEGATIVE VALUE CASES
    # =========================

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            store_patient_details("Test", -1, "Male", "9000000005")

    def test_age_exceeds_limit(self):
        with self.assertRaises(ValueError):
            store_patient_details("Test", 150, "Male", "9000000006")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            store_patient_details("", 25, "Female", "9000000007")

    def test_name_too_long(self):
        with self.assertRaises(ValueError):
            store_patient_details("A" * 51, 30, "Male", "9000000008")

    def test_invalid_gender_value(self):
        with self.assertRaises(ValueError):
            store_patient_details("Alex", 30, "Other", "9000000009")

    def test_contact_less_than_10_digits(self):
        with self.assertRaises(ValueError):
            store_patient_details("Ravi", 40, "Male", "12345")

    def test_contact_more_than_10_digits(self):
        with self.assertRaises(ValueError):
            store_patient_details("Ravi", 40, "Male", "123456789012")

    def test_contact_with_characters(self):
        with self.assertRaises(ValueError):
            store_patient_details("Ravi", 40, "Male", "98A6543210")

    # =========================
    # ❌ TYPE VALIDATION CASES
    # =========================

    def test_name_wrong_type(self):
        with self.assertRaises(TypeError):
            store_patient_details(123, 30, "Male", "9000000010")

    def test_age_wrong_type(self):
        with self.assertRaises(TypeError):
            store_patient_details("Ravi", "Thirty", "Male", "9000000011")

    def test_gender_wrong_type(self):
        with self.assertRaises(TypeError):
            store_patient_details("Ravi", 30, 1, "9000000012")

    def test_contact_wrong_type(self):
        with self.assertRaises(TypeError):
            store_patient_details("Ravi", 30, "Male", 9876543210)


if __name__ == "__main__":
    unittest.main()
