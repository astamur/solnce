"""
Пузырьковая сортивка.
"""


# O(N * (4 * (N/2)) ~ O(N^2)
def sort(nums):
    length = len(nums)
    swapped = True

    print("Nums: {}".format(nums))

    # N
    for i in range(len(nums)):
        if not swapped:
            return

        swapped = False

        # N/2
        for j in range(1, length - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                swapped = True
        print("Nums: {}".format(nums))


# Example
nums = [9, 2, 6, 3, 1, 7, 4, 2, 8]
sort(nums)
print(nums)
