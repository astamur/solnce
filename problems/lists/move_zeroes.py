"""
Дан список чисел. Напишите функцию, которая сдвигает все нули в конец массива, сохраняя порядок не-нулевых чисел.
Пример: [0,1,0,3,12] -> [1,3,12,0,0].
"""


def move_zeroes(nums):
    position = 0

    # [1, 2, 3, 0, 4, 5]
    # position=0, n=1: [1, 2, 3, 0, 4, 5]
    # position=1, n=2: [1, 2, 3, 0, 4, 5]
    # position=2, n=3: [1, 2, 3, 0, 4, 5]
    # position=3, n=0: [1, 2, 3, 0, 4, 5]
    # position=3, n=4: [1, 2, 3, 4, 4, 5]
    # position=4, n=5: [1, 2, 3, 4, 5, 5]
    for n in nums:
        if n != 0:
            nums[position] = n
            position += 1

    # position=5: [1, 2, 3, 4, 5, 0]
    while position < len(nums):
        nums[position] = 0
        position += 1


def move_zeroes_2(nums):
    count = nums.count(0)
    nums = [n for n in nums if n != 0]

    for i in range(count):
        nums.append(0)

    return nums


nums1 = [0, 1, 14, 1, 21, 1, 0, 0, 4, 5]
nums2 = [0, 1, 14, 1, 21, 1, 0, 0, 4, 5]

move_zeroes(nums1)

print(nums1)
print(move_zeroes_2(nums2))
