"""
Пузырьковая сортивка.
"""


# O(N*(N/2)) ~ O(N^2)
def sort(nums):
    length = len(nums)
    step = 0

    print("Nums: {}".format(nums))

    # N
    while step < length:
        # N/2
        for i in range(1, length - step):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
        print("Nums: {}".format(nums))
        step += 1

    return nums


# Example
print(sort([9, 2, 6, 3, 1, 7, 4, 2, 8]))
