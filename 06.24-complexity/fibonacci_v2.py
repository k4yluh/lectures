import sys


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # NOTE: The number of operations performed includes the numbers of the
        #       two recursive calls. By def'n, f(n - 1) = f(n - 2) + f(n - 3).
        #       By recursively computing f(n - 1), we have *already* computed
        #       f(n - 2) -- it is wildly inefficient to do it again.
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
