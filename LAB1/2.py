import unittest
import first

class TwoSum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(first.TwoSum().two_sum([1, 6, 8, 14], 20), (1, 3))

    def test_with_duplicates(self):
        self.assertEqual(first.TwoSum().two_sum([4, 11, 15, 4], 8), (0, 3))

    def test_end_of_list(self):
        self.assertEqual(first.TwoSum().two_sum([100, 200, 25, 50], 75), (2, 3))

    def test_with_identical_pair(self):
        self.assertEqual(first.TwoSum().two_sum([5, 12, 5], 10), (0, 2))

if __name__ == '__main__':
    unittest.main()
