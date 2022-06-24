import sys


def fibonacci(n):
    # In order to avoid computing any number twice, we could instead return
    #  both the nth number and the (n - 1)st.
    if n == 0:
        return (None, 0)
    elif n == 1:
        return (0, 1)
    else:
        previous, current = fibonacci(n - 1)
        return (current, current + previous)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
