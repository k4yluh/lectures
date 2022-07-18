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
