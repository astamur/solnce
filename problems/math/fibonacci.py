"""
Найти и распечатать ряд чисел Фибоначчи, не превышащих заданного значения `target`
"""


def fib(target):
    a, b, c = 1, 1, 1

    while c <= target:
        print(c)
        c = a + b
        a, b = b, c


fib(10)
