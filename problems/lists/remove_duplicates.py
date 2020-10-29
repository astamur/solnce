"""
Дан отсортированный список чисел. Нужно удалить в нем дубликаты и
вернуть новую длину списка. Можно менять данные в исходном списке.
Ограничение по памяти O(1).
Пример: [0,0,1,1,1,2,2,3,3,4] -> 5
(при этом, в списке будут значения [0,1,2,3,4,....]).
"""


def remove_duplicates(nums):
    tail = 0

    # tail=0, i=1: [0,0,1,1,1,2,2,3,3,4]
    # tail=0, i=2: [0,1,1,1,1,2,2,3,3,4]
    # tail=1, i=3: [0,1,1,1,1,2,2,3,3,4]
    # tail=1, i=4: [0,1,1,1,1,2,2,3,3,4]
    # tail=1, i=5: [0,1,2,1,1,2,2,3,3,4]
    # tail=2, i=6: [0,1,2,1,1,2,2,3,3,4]
    # tail=2, i=7: [0,1,2,3,1,2,2,3,3,4]
    # tail=3, i=8: [0,1,2,3,1,2,2,3,3,4]
    # tail=3, i=9: [0,1,2,3,4,2,2,3,3,4]
    # O(3 * N) -> O(N)
    for i in range(1, len(nums)):
        if nums[i] != nums[tail]:
            tail += 1
            nums[tail] = nums[i]
        print(nums)

    return tail + 1


def remove_duplicates_2(nums):
    res = set()

    for n in nums:
        res.add(n)

    print(res)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(nums)

print(nums[0:remove_duplicates(nums)])
print(nums)
