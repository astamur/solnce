"""
Дан спсиок чисел, состоящий из 0 и 1.
Найти длину максимальной последовательности из единиц.
"""


def find(nums):
    counter = 0
    max_len = 0

    for n in nums:
        if n == 1:
            counter += 1
        else:
            max_len = max(counter, max_len)
            counter = 0

    return max(counter, max_len)


numbers = [1, 1, 1, 0, 1, 1, 1, 1]
result = find(numbers)

print(numbers)
print("Результат: %s" % result)
