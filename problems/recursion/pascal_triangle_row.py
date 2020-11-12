"""
Вернуть строку с заданным номером из Треугольника Паскаля. Нумерация строк с 0. Пример: 3 ->[1,3,3,1]
"""


def get_row(row):
    """
    Простая рекурсия
    """
    res = list()

    for i in range(row + 1):
        res.append(get_num(row, i))

    return res


def get_num(row, col):
    print("row = {}, col = {}".format(row, col))

    if row == 0 or col == 0 or col == row:
        return 1

    return get_num(row - 1, col - 1) + get_num(row - 1, col)


def get_row_memo(row):
    """
    Простая рекурсия с запоминанием предыдущих вычислений
    """
    res = list()
    memo = {}

    for i in range(row + 1):
        res.append(get_num_memo(row, i, memo))

    return res


def get_num_memo(row, col, memo):
    key = "{}|{}".format(row, col)  # 1|1

    print(memo)

    val = -1
    if key in memo:
        return memo[key]
    elif row == 0 or col == 0 or col == row:
        val = 1
    else:
        val = get_num_memo(row - 1, col - 1, memo) + get_num_memo(row - 1, col, memo)

    memo[key] = val

    return val


def dp(row):
    """
    Решение с использованием Динамического Программирования (Dynamic Programming)
    """
    res = [1] * (row + 1)

    print(res)

    for i in range(2, row + 1):
        for j in range(i - 1, 0, -1):
            res[j] += res[j - 1]
        print(res)
    return res


# Example 1
# print(get_row(3))

# Example 2
# print(get_row_memo(10))

# Example 3
print(dp(5))
