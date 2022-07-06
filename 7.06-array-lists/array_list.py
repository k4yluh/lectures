class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # NOTE: Python does not have true arrays, but we can pretend that its
        #       built-in lists are "arrays" by ignoring all of their extra
        #       features beyond simple indexing.
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0


def get(lst, idx):
    # Return array[idx].
    pass


def set(lst, idx, value):
    # Set array[idx] to value.
    pass


def add(lst, idx, value):
    # If the size is equal to the capacity:
    #     Double the capacity.
    #     Create a new array with that new capacity.
    #     For i from 0 to the size of the list:
    #         Set new_array[i] to array[i].
    #     Set the list's array to that new array.
    # For i from idx to the size of the list:
    #     Shift array[i] down to array[i + 1].
    # Set array[idx] to value.
    pass


def remove(lst, idx):
    # Set a temporary variable to array[idx].
    # For i from idx to the size of the list:
    #     Shift array[i + 1] up to array[i].
    # Return the temporary variable.
    pass
