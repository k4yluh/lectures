class SortedList:
    """ A sorted collection of elements """

    # NOTE: The list must be sorted in order to perform a binary search, else
    #       comparing the middle element eliminates only the middle element.

    # NOTE: The list must be backed by an array, so that it can support fast
    #       random access. With a linked list, comparing the midpoint instead
    #       of the first element saves no time, because simply getting to the
    #       midpoint requires traversing the entire first half.

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0


def find(lst, value):
    # NOTE: Every comparison eliminates about half the remaining elements;
    #       in the worst case scenario, the number of comparisons is equal to
    #       the number of times the list can be halved until it is empty: this
    #       is the number of times n can be divided by 2: approx. log_2 n.

    # Set low to 0 and high to size - 1.
    # While low <= high:
    #     Set mid to (low + high) // 2.
    #     If array[mid] < value:
    #         NOTE: Could also recurse on a smaller list.
    #         Set low to mid + 1.
    #     Else if array[mid] > value:
    #         NOTE: Could also recurse on a smaller list.
    #         Set high to mid - 1.
    #     Else:
    #         Return mid
    # Return None
