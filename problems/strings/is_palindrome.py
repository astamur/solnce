"""
Дана строка. Нужно определить, является ли эта строка палиндромом. Пример: "abcdefgfedcba" -> true.
"""


def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


print(is_palindrome("AbCdefgfedcBa"))
print(is_palindrome("aabbceedd"))
