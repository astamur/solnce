def recursive(n):
    if n < 0:
        return

    print(n)
    recursive(n-1)


recursive(10)
