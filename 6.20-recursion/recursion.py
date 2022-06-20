# To find the largest element in a list by "recursing on" the list:
def max_element(lst):
    """
    Find the largest element in a list.

    :param lst: An instance of a problem -- a list of comparable elements
    :return: The solution to that problem -- the largest element, or None
    """
    # The "base cases" of a recursive function should solve the smallest
    #  possible instances of the problem -- lists of 0 or 1 elements.
    if len(lst) == 0:
        print("The solution to the problem of " + repr(lst)
              + " is " + repr(None))
        return None
    elif len(lst) == 1:
        print("The solution to the problem of " + repr(lst)
              + " is " + repr(lst[0]))
        return lst[0]

    # The "recursive cases" of a recursive function should solve larger
    #  problems by reducing them to smaller problems -- removing the first
    #  element from the list yields a smaller instance of the same problem.
    temp = max(lst[0], max_element(lst[1:]))
    print("The solution to the problem of " + repr(lst) + " is " + repr(temp))
    return temp


print(max_element([2, -1, 9, 8, 5, -3, 0, 8]))
