import unittest
import first

class TestMySolution(unittest.TestCase):

    def test_same_lst_elems(self):
        self.assertEqual(first.Solution().two_sum([3, 8, 12, 17], 11), (0, 1))
        self.assertEqual(first.Solution().two_sum([5, 5, 5, 5], 10), (0, 1))
        self.assertEqual(first.Solution().two_sum([10, 20, 30, 40], 70), (2, 3))

if __name__ == '__main__':
    unittest.main()
