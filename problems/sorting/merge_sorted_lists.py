"""
Даны 2 отсортированных списка c целыми числами nums1 и nums2. Нужно добавить элементы из nums2 в nums1,
чтобы получился один отсортированный список. Количество элементов в nums1 и nums2 равно m и n соответственно.
Длина списка nums1 равна m + n, чтобы можно было уместить в него все элементы из nums2.
Пример: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 -> [1,2,2,3,5,6]
"""


def merge(nums1, m, nums2, n):
    print("{}, {}".format(nums1, nums2))
    print("{}, m = {}, n = {}".format(nums1, m, n))

    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        print("{}, m = {}, n = {}".format(nums1, m, n))
    if n > 0:
        nums1[:n] = nums2[:n]


# Пример
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)
print(nums1)
