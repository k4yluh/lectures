class SortedList:
    """ A sorted collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0


def find(lst, value):
    # Set low to 0 and high to size - 1.
    # While low <= high:
    #     Set mid to (low + high) // 2.
    #     If array[mid] < value:
    #         Set low to mid + 1.
    #     Else if array[mid] > value:
    #         Set high to mid - 1.
    #     Else:
    #         Return mid
    # Return None


def insert(lst, value):
    # NOTE: The best-case scenario is that the value is bigger than any
    #       element in the list: O(1)
    #       The worst-case scenario is that the value is smaller than any
    #       element in the list: O(n)
    #       The average-case scenario is that the value is somewhere around
    #       the midpoint of the list: n/2 = O(n)

    # If size == capacity:
    #     Double the capacity...
    # For i from size - 1 down to 0:
    #     If array[i] <= value:
    #          array[i + 1] = value
    #          Increment the size.
    #          Return.
    #     Else:
    #          array[i + 1] = array[i]
    # Set array[0] = value.
    # Increment the size.
    # Return.


def create(lst):
    # NOTE: The best-case scenario is that the list is already sorted, and
    #       each element is thus larger than any prior: O(n)
    #       The worst-case scenario is that the list sorted in reverse, and
    #       each element is thus smaller than any prior: O(n^2)
    #       The average-case scenario is that each element is roughly the
    #       median of those prior: n * n/2 = O(n^2)

    # Make a new sorted list.
    # For every element in the list:
    #     Insert the element into the sorted list.
    # Return the sorted list.
