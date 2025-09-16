# script_solution.py

# Исходные данные для примера
arr = [2, 7, 11, 15]
i = 9

class Solution:
    """Решает задачу Two Sum методом перебора."""

    def two_sum(self, lst, target):
        for x in range(len(lst)):
            temp = lst[x + 1:]
            if target - lst[x] in temp:
                return (x, temp.index(target - lst[x]) + x + 1)

# --- Примеры использования ---

# Создаем экземпляр класса
my_solution = Solution()

# Вызов с одними данными
res = my_solution.two_sum([16, 2, 15, 89], 105)
print(f"Результат для [16, 2, 15, 89] и 105: {res}")

# Вызов с другими данными
print(f"Результат для {arr} и {i}: {my_solution.two_sum(arr, i)}")
