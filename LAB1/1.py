numbers = [4, 8, 15, 16, 23, 42]
target_sum = 31

class TwoSum:
    def two_sum(self, nums, target):
        num_map = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return (num_map[complement], index)
            num_map[num] = index

my_solver = TwoSum()

result1 = my_solver.two_sum([3, 9, 11, 17], 20)
print(f"Результат для первого вызова: {result1}")

result2 = my_solver.two_sum(numbers, target_sum)
print(f"Результат для второго вызова: {result2}")
