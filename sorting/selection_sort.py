"""
Сортировка выбором.
"""


# O(N * (2 *(N/2) + 3)) ~ O(N^2)
def sort(nums):
    print("Nums: {}".format(nums))

    # N
    for i in range(len(nums)):
        min_index = i

        # N/2
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        # 3
        nums[i], nums[min_index] = nums[min_index], nums[i]
        print("Nums: {}".format(nums))


# Example
nums = [9, 2, 6, 3, 1, 7, 4, 2, 8]
sort(nums)
print(nums)
