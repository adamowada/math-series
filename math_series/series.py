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


# https://linux.die.net/diveintopython/html/power_of_introspection/optional_arguments.html 
# helped me with optional parameters
def sum_series(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    # https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python 
    # helped me with line continuation
    count = sum_series(n-1, first, second) + \
        sum_series(n-2, first, second)
    return count
