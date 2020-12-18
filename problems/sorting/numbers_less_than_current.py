"""
Дан список чисел nums. Для каждого числа из списка нужно найти количество чисел из nums, которые меньше него самого.
Ограничения: 2 <= nums.length <= 500 и 0 <= nums[i] <= 100. Пример: [8,1,2,2,3] -> [4,0,1,1,3].
"""


# O(N*N)
def find1(nums):
    result = []

    # N
    for i in range(len(nums)):
        count = 0
        # N
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1
        result.append(count)

    return result


# O(N*log(N))
def find2(nums):
    """
    Using a default sort (Quick Sort).
    """
    print("Nums: \t\t{}".format(nums))

    map = {}

    # O(N*log(N))
    sortedNums = sorted(nums)

    # O(N)
    for index, n in enumerate(sortedNums):
        map.setdefault(n, index)
        print("Index, n: {}, {}. Map: {}".format(index, n, map))

    # result = []
    # for n in nums:
    #     result.append(map[n])
    # return result

    return [map[n] for n in nums]


# N - длина исходного списка
# M - количество уникальных чисел (в примере их 100)
# O(N + M + N) ~ O(N)
def find3(nums):
    """
    Using a counting sort.
    """
    print("Nums: {}".format(nums))

    counts = [0] * 102

    print("Counts: {}".format(counts[:20]))

    # O(N)
    for n in nums:
        counts[n + 1] += 1

    print("Counts: {}".format(counts[:20]))

    # O(M)
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    print("Counts: {}".format(counts[:20]))

    # O(N)
    # result = []
    # for n in nums:
    #     result.append(counts[n])
    # return result

    return [counts[n] for n in nums]


# Example
# print(find1([8, 1, 2, 2, 3]))
# print(find2([8, 1, 8, 2, 3, 2, 1, 3]))
print(find3([8, 10, 15, 5, 1, 4, 2, 7, 7, 9, 12, 2, 3]))
