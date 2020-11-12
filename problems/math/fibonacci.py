"""
Найти и распечатать ряд чисел Фибоначчи, не превышащих заданного значения `target`
"""


def fib(target):
    a = 0
    b = 1

    while b <= target:
        print("a = {}, b = {}, c = {}".format(a, b, b))
        a, b = b, a + b
