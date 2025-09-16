import unittest
import first

# Класс TwoSum для тестирования моего решения
class TwoSum(unittest.TestCase):

    def test_positive_numbers(self):
        # Проверка на простом массиве с положительными числами
        self.assertEqual(first.Solution().two_sum([1, 6, 8, 14], 20), (1, 3))

    def test_with_duplicates(self):
        # Проверка, когда в массиве есть одинаковые числа
        self.assertEqual(first.Solution().two_sum([4, 11, 15, 4], 8), (0, 3))

    def test_end_of_list(self):
        # Проверка, когда нужная пара находится в конце списка
        self.assertEqual(first.Solution().two_sum([100, 200, 25, 50], 75), (2, 3))

if __name__ == '__main__':
    unittest.main()
