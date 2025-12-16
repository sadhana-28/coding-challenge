import unittest

class TestLevel3FetchCosts(unittest.TestCase):

    # ✅ Positive case: valid indices
    def test_valid_indices(self):
        costs = [500, 300, 800, 1500]
        self.assertEqual(fetch_costs(costs, [0, 3]), [500, 1500])

    # ⚠️ Edge case: empty indices list
    def test_empty_indices(self):
        costs = [500, 300]
        self.assertEqual(fetch_costs(costs, []), [])

    # ⚠️ Edge case: single index
    def test_single_index(self):
        costs = [500, 300]
        self.assertEqual(fetch_costs(costs, [1]), [300])

    # ❌ Negative case: index out of range
    def test_index_out_of_range(self):
        costs = [500, 300]
        with self.assertRaises(IndexError):
            fetch_costs(costs, [5])

    # ❌ Negative case: negative index
    def test_negative_index(self):
        costs = [500, 300]
        with self.assertRaises(IndexError):
            fetch_costs(costs, [-1])


if __name__ == "__main__":
    unittest.main()
