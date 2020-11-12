"""
Найти сумму членов последовательности Фибоначчи, являющихся четными числами и не превышающих 4 миллиона.
"""

import datetime


def sum(limit):
    prev, cur, sum = 1, 2, 0

    while cur < limit:
        if cur % 2 == 0:
            sum += cur

        prev, cur = cur, prev + cur

    return sum


def sum_2(limit):
    prev, cur, sum = 1, 2, 0
    prev_even, cur_even = False, True

    while cur < limit:
        if cur_even:
            sum += cur

        prev_even, cur_even = cur_even, (prev_even and cur_even) or (not prev_even and not cur_even)
        prev, cur = cur, prev + cur

    return sum


start = datetime.datetime.now()
print(sum(10000000000000000))
print("Функция 1. Прошло: %s" % (datetime.datetime.now() - start))


start = datetime.datetime.now()
print(sum_2(10000000000000000))
print("Функция 1. Прошло: %s" % (datetime.datetime.now() - start))
