def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    count = fibonacci(n-1) + fibonacci(n-2)
    return count


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    count = lucas(n-1) + lucas(n-2)
    return count


