import unittest

class TestLevel7AdminSetup(unittest.TestCase):

    # ✅ Positive case: valid service
    def test_add_valid_service(self):
        services = []
        costs = []
        add_service(services, costs, "MRI", 7000)
        self.assertEqual(services, ["MRI"])
        self.assertEqual(costs, [7000])

    # ⚠️ Edge case: zero cost service
    def test_zero_cost_service(self):
        services = []
        costs = []
        add_service(services, costs, "Free Checkup", 0)
        self.assertEqual(costs[0], 0)

    # ❌ Negative case: negative cost
    def test_negative_cost(self):
        services = []
        costs = []
        with self.assertRaises(ValueError):
            add_service(services, costs, "X-Ray", -500)

    # ❌ Negative case: empty service name
    def test_empty_service_name(self):
        services = []
        costs = []
        with self.assertRaises(ValueError):
            add_service(services, costs, "", 500)


if __name__ == "__main__":
    unittest.main()
