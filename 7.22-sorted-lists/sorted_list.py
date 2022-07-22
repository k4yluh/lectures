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
    # NOTE: At each step, we halve the list. The number of times the list can
    #       be halved is approximately log_2 n.
    #       At each step, we merge the halves. Each merge is O(n).
    #       The entire sort is O(n log n), which is better than O(n^2).

    # If the list has size 1:
    #     Good job.
    # Else:
    #     Make two new lists by splitting the given list into two.
    #     Recursively sort the two halves.
    #     NOTE: By the time those recursive calls return, both halves must
    #           have been completely sorted.
    #     Merge the two halves together.


def merge(lst_a, lst_b):
    # Make a new list with capacity for lst_a's size + lst_b's size.
    # Set i and j to 0.
    # While i < lst_a's size or j < lst_b's size:
    #     If i >= lst_a's size:
    #         Append lst_b[j] to the new list.
    #         Increment j.
    #     Else if j >= lst_b's size:
    #         Append lst_a[i] to the new list.
    #         Increment i.
    #     Else if lst_a[i] < lst_b[j]:
    #         Append lst_a[i] to the new list.
    #         Increment i.
    #     Else:
    #         Append lst_b[j] to the new list.
    #         Increment j.
    # Return the new list.
