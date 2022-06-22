import sys


# To compute the nth Fibonacci number iteratively:
# def fibonacci(n):
#     current = previous = None
#
#     for i in range(n + 1):
#         if i == 0:
#             current = 0
#         elif i == 1:
#             previous = current
#             current = 1
#         else:
#             temp = previous
#             previous = current
#             current = current + temp
#
#         print("previous = %s, current = %s" % (repr(previous), repr(current)))
#
#     return current


# To compute the nth Fibonacci number recursively:
def fibonacci(n):
    # The base cases should address the smallest possible problems -- since
    #  the Fibonacci numbers are recursively defined, that definition tells
    #  us what the smallest possible problems and their solutions are.
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # The recursive cases should reduce larger problems into smaller problems
    #  -- since the Fibonacci numbers are recursively defined, that definition
    #  tells us how smaller problems fit into larger problems.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(fibonacci(int(sys.argv[1])))
