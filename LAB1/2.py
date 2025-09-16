# test_solution.py

import unittest

# Класс с решением копируется прямо в этот файл,
# чтобы не было зависимости от другого файла.
class Solution:
    """Решает задачу Two Sum методом перебора."""

    def two_sum(self, lst, target):
        for x in range(len(lst)):
            temp = lst[x + 1:]
            if target - lst[x] in temp:
                return (x, temp.index(target - lst[x]) + x + 1)


# --- Юнит-тесты для проверки класса Solution ---

class TestMySolution(unittest.TestCase):

    def test_same_lst_elems(self):
        # Создаем экземпляр локального класса Solution
        solver = Solution()
        self.assertEqual(solver.two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(solver.two_sum([3, 3, 3, 3], 6), (0, 1))
        self.assertEqual(solver.two_sum([16, 2, 15, 89], 105), (0, 3))

# Эта строка запускает все тесты в файле
if __name__ == '__main__':
    unittest.main()
