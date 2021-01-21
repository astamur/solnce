"""
Сортировка слиянием.
"""


def sort_top_down(a):
    """
    Сортировка слиянием "сверху-вниз"
    """
    print(a)

    # O(logN * N)
    # Память O(N)
    def sort(a, aux, low, high):
        print("Sort Top-Down. low={}, high={}".format(low, high))

        if high <= low:
            return

        mid = low + (high - low) // 2
        sort(a, aux, low, mid)
        sort(a, aux, mid + 1, high)
        merge(a, aux, low, mid, high)

    aux = [0] * len(a)
    sort(a, aux, 0, len(a) - 1)


def sort_bottom_up(a):
    """
    Сортировка слиянием "снизу-вверх"
    """
    print(a)

    n = len(a)
    aux = [0] * n
    i = 1
    while i < n:
        j = 0
        while j < n - i:
            low = j
            mid = j + i - 1
            high = min(j + i * 2 - 1, n - 1)
            print("Sort Bottom-Up. i={}, j={}, low={}, mid={}, high={}".format(i, j, low, mid, high))
            merge(a, aux, low, mid, high)
            j += i * 2
        i *= 2


# O(N)
def merge(a, aux, low, mid, high):
    for k in range(low, high + 1):
        aux[k] = a[k]

    i, j = low, mid + 1
    for k in range(low, high + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > high:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

    print("{}. low={}, mid={}, high={}".format(a, low, mid, high))


# Example Top-Down
# nums = [6, 2, 9, 3, 7, 8, 4, 1, 3, 5, 7, 9, 2]
# sort_top_down(nums)
# print(nums)

# Example Bottom-Up
nums = [6, 2, 9, 3, 7, 8, 4, 1, 3, 5, 7, 9, 2]
sort_bottom_up(nums)
print(nums)
