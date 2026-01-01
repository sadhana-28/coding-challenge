import unittest

class TestLevel2(unittest.TestCase):

    services = ["Consultation", "Blood Test", "X-Ray"]

    # ✅ Positive
    def test_valid_selection(self):
        self.assertEqual(
            select_services(self.services, [0, 2]),
            ["Consultation", "X-Ray"]
        )

    # ⚠️ Edge
    def test_empty_selection(self):
        self.assertEqual(select_services(self.services, []), [])

    # ❌ Invalid index
    def test_out_of_range(self):
        with self.assertRaises(IndexError):
            select_services(self.services, [5])

    # ❌ Wrong type
    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            select_services(self.services, ["1"])
