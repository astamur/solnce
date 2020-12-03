"""
Дан массив уникальных целых чисел. Вернуть все подмножества из данного массива в любом порядке.
Пример: [1,2,3] -> [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]
"""


def subsets(nums):
    def backtrack(size, first=0, subset=[]):
        if len(subset) == size:
            result.append(subset[:])
            return

        for i in range(first, n):
            subset.append(nums[i])
            backtrack(size, i + 1, subset)
            subset.pop()

    result = []
    n = len(nums)

    for i in range(n + 1):
        backtrack(i)

    return result


# Example
print(subsets([1, 1, 2, 3]))
