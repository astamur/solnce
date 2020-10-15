import random
import datetime

"""
Дан список целых чисел, отсортированный в порядке не-убывания.
Вернуть список квадратов этих чисел, также расположенных в порядке не-убывания.
Например, [-3 ,-2, -1, 0, 1, 2, 3] -> [0, 1, 1, 4, 4, 9, 9].
"""

# [-3 ,-2, -1, 0, 1, 2, 3]   O(logN)
# 2**3 = 8  -> log2(8) = 3
# 3**4 = 27  -> log3(27) = 4

# 0: [3 ,1, -1, 3, -3, -2, 2, 0]    N
# 1: [-3, 1, -1, 3, 3, -2, 2, 0]    N-1
# 2: [-3, -2, -1, 3, 3, 1, 2, 0]    N-2
# 3: [-3, -2, -1, 3, 3, 1, 2, 0]    N-3
# 4: [-3, -2, -1, 0, 3, 1, 2, 3]    N-4
# 5: [-3, -2, -1, 0, 1, 3, 2, 3]    N-5
# 6: [-3, -2, -1, 0, 1, 2, 3, 3]    N-6
# 7: [-3, -2, -1, 0, 1, 2, 3, 3]    N-7
# 8: [-3, -2, -1, 0, 1, 2, 3, 3]    N-8
# O(N*N)

# O(N*log(N))


def calculate_squares_1(nums):
    # N - длина исходного списка
    result = []

    # O(N)
    for i in nums:
        result.append(i**2)

    # O(N*log(N))
    return sorted(result)
# Total: O(N + N*log(N)) -> O(N*log(N)) - линейно-логарифмическая сложность


def calculate_squares_2(nums):
    # N - длина исходного списка
    result = []
    left, right = 0, len(nums) - 1

    # O(N)
    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result.append(nums[left]**2)
            left += 1
        else:
            result.append(nums[right] ** 2)
            right -= 1

    # O(N)
    return result[::-1]
# Total: O(N + N) -> O(N)


nums = []
for i in range(10000000):
    nums.append(i)

random.shuffle(nums)

start = datetime.datetime.now()
calculate_squares_1(nums)
print("Функция 1. Прошло: %s" % (datetime.datetime.now() - start))

start = datetime.datetime.now()
calculate_squares_2(nums)
print("Функция 2. Прошло: %s" % (datetime.datetime.now() - start))
