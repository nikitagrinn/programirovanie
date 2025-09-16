# Задаем мой массив и итоговую сумму
numbers = [4, 8, 15, 16, 23, 42]
target_sum = 31

class TwoSum:
    '''
    Этот класс находит пару чисел в списке,
    сумма которых равна заданному значению.
    '''

    def two_sum(self, lst, target):
        # Проходим по каждому элементу списка
        for x in range(len(lst)):
            # Создаем временный список из оставшихся элементов
            temp = lst[x + 1:]
            # Ищем второе число для пары
            if target - lst[x] in temp:
                # Если нашли, возвращаем индексы обоих чисел
                return (x, temp.index(target - lst[x]) + x + 1)

# Создаем экземпляр моего класса
my_solver = TwoSum()

# Первый вызов с новыми данными
result1 = my_solver.two_sum([3, 9, 11, 17], 20)
print(f"Результат для первого вызова: {result1}")

# Второй вызов с использованием переменных
result2 = my_solver.two_sum(numbers, target_sum)
print(f"Результат для второго вызова: {result2}")
