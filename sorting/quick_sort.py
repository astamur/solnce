"""
Быстрая сортировка.
"""

import random


def sort(arr):
    def shuffle():
        n = len(arr)
        for i in range(n):
            r = i + random.randint(0, n - i - 1)
            arr[i], arr[r] = arr[r], arr[i]

    def sort(low, high):
        if high <= low:
            return

        point = partition(low, high)
        sort(low, point - 1)
        sort(point + 1, high)

    def partition(low, high):
        i, j, v = low + 1, high, arr[low]

        while True:
            while arr[i] < v and i != high:
                i += 1
            while v < arr[j] and j != low:
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

        arr[low], arr[j] = arr[j], arr[low]
        print(arr)
        print("==========================")
        return j

    print(arr)
    shuffle()
    print(arr)
    print("==========================")
    sort(0, len(arr) - 1)


# Пример
nums = [10, 5, 7, 3, 9, 2, 6, 4, 1, 8]
sort(nums)
print(nums)
