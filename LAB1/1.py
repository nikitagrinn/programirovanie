arr = [5, 12, 18, 21]
i = 23


class Solution:
    '''Returns solutions'''

    def two_sum(self, lst, target):
        '''Returns two_sum\'s solution'''

        for x in range(len(lst)):
            temp = lst[x + 1:]
            if target - lst[x] in temp:
                return (x, temp.index(target - lst[x]) + x + 1)


my_solution = Solution()
res = my_solution.two_sum([10, 20, 30, 40], 50)
print(res)

print(my_solution.two_sum(arr, i))
