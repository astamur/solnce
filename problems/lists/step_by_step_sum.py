"""
Дан список чисел nums. Начиная с некоторого положительного числа startValue, шаг за шагом,
мы считаем сумму startValue и чисел из списка nums (слева направо).
Нужно найти такое минимальное значение startValue, чтобы на каждом шаге эта сумма была >= 1.
Пример: [-3,2,-3,4,2] -> 5 (минимальное значение суммы будет равно 1 на 3 шаге).
"""


def find(nums):
    min_sum = 0
    sum = 0

    for n in nums:
        sum += n
        # min_sum = min(min_sum, sum)
        if sum < min_sum:
            min_sum = sum

    # print(min_sum)

    return -min_sum + 1 if (min_sum < 0) else 1


# Example
print(find([-3, 2, -3, 4, 2]))
