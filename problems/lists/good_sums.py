"""
Дан список чисел nums. Будем называть пару (i, j) "хорошей", если nums[i] == nums[j] и i < j.
Вернуть количество таких пар. Ограничение по значениям: 1 <= nums[i] <= 100. Пример: [1,2,3,1,1,3] -> 4
"""


def find(nums):
    n = len(nums)
    kol = 0
    sorted(nums)

    # [1,1,1,2,3,3]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                kol += 1
                print(kol)
    return kol


# Example
print("Total: {}".format(find([1, 2, 3, 1, 1, 3])))
