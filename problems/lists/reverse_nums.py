"""
Дан список чисел. Напишите функцию, которая разворачивает его. Не выделяйте дополнительное пространство для
другого списка. Нужно сделать это, изменив исходный список (in-place) с помощью дополнительной памяти O(1) (константно).
Пример: [1,2,3,4,5] -> [5,4,3,2,1].
"""


def reverse_nums(nums):
    # left, right = 0, len(nums) - 1

    # O(5 * (N/2))
    # while left < right:
    #     nums[left], nums[right] = nums[right], nums[left]
    #     left, right = left + 1, right - 1

    nums_len = len(nums) - 1
    # O(4 * (N/2))
    for i in range(0, len(nums) // 2):
        nums[i], nums[nums_len-i] = nums[nums_len-i], nums[i]


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_nums(nums)
print(nums)
