"""
Дана матрица accounts размером m x n (m на n), состоящая их целых чисел.
Каждый элемент accounts[i][j] представляет количество денег клиента i в банке j.
Найти общее состояние самого богатого клиента.
Пример: [[1,5],[7,3],[3,5]] -> 10
"""


# O(N*M)
def find(accounts):
    max_sum = 0

    # N
    for i in range(len(accounts)):
        sum = 0
        # M
        for j in range(len(accounts[i])):
            sum += accounts[i][j]
        max_sum = max(max_sum, sum)

    print(max_sum)


# Example
find([[1, 5], [7, 3], [3, 5]])
