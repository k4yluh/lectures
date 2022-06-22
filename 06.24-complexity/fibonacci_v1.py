import sys


def fibonacci(n):
    current = previous = None

    for i in range(n + 1):
        if i == 0:
            current = 0
        elif i == 1:
            previous = current
            current = 1
        else:
            temp = previous
            previous = current
            current = current + temp

    return current


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
