"""
Дано целое число. Найти сумму его цифр.
Пример: 123 -> 1 + 2 + 3 -> 6
"""


def sum_of_digits(number):
    s = 0

    while number != 0:
        s += number % 10
        number //= 10

    return s


number = 12345
print("Сумма чисел %s равна %s" % (number, sum_of_digits(number)))
