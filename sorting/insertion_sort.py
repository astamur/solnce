"""
Сортивка вставками.
"""


# O(N^2)
def sort(nums):
    print("Nums: {}".format(nums))

    # N
    for i in range(1, len(nums)):
        print("==========================================")
        j = i - 1
        current = nums[i]

        print("Nums: {}. i: {}. j: {}. current: {}".format(nums, i, j, current))

        # N
        while j >= 0 and current < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
            print("Nums: {}. i: {}. j: {}. current: {}".format(nums, i, j, current))
        nums[j + 1] = current
        print("Nums: {}. i: {}. j: {}. current: {}".format(nums, i, j, current))


# Example
# nums = [9, 2, 6, 3, 1, 7, 4, 2, 8]
# nums = [1, 2, 2, 3, 4, 6, 7, 8, 9]
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort(nums)
print(nums)
