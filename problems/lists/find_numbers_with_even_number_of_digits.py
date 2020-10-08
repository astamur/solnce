"""
Дан список челых чисел.
Найти количество чисел в нем, которые состоят из
четного количества цифр.
"""


def find(nums):
    total = 0
    for n in nums:
        if number_length(n) % 2 == 0:
            total += 1

    return total


def number_length(number):
    num_length = 0

    while number != 0:
        num_length += 1
        number //= 10

    return num_length


numbers = [1, 12, 123, 1234, 12345]
result = find(numbers)

print(numbers)
print("Результат: %s" % result)
