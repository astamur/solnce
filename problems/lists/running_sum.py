"""
Дан список чисел nums. Определим "бегущую сумму" (running sum), как runningSum[i] = sum(nums[0] + ... +nums[i]).
Нужно вернуть список, состоящий их таких сумм. Пример: [1,1,1,1,1] -> [1,2,3,4,5]
"""


# Вариант 1: N * (N/2 * (N/2)) ~ O(N^2)
# Вариант 2: N * (5) ~ O(N)
def calculate_sum(nums):
    n = len(nums)
    result = [nums[0]]

    # i: 1, result: [1]
    # i: 2, result: [1, result[i-1] + nums[i]]
    # i: 3, result: [1, 2, result[i-1] + nums[i]]
    # ...

    for i in range(1, n):
        result.append(result[i - 1] + nums[i])
        print("Step: {}. Array: {}".format(i, result))

    return result


# Example
print(calculate_sum([1, 1, 1, 1, 1]))

# [1,2,3,4,5,6,7,8,9,10] - Найти 9?
# Варинт 1: O(N/2) ~ O(N) - линейная сложность
# Варинт 2: O(log(N)) ~ O(N) - линейная сложность

# O(N * (log(N))) ~ O(NlogN)

