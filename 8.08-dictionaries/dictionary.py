class Dictionary:
    """ A collection of key-value pairs """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0


def get(dct, key):
    # Hash the given key and mod it by the capacity.
    # Return the element in the array at that hash code.
    pass


def insert(dct, key, value):
    # NOTE: This only works as long as every key is guaranteed to perfectly
    #       hash to its own unique index -- which, in general, is not a safe
    #       assumption. Essentially, each array location needs to be able to
    #       contain more than one value, should their keys hash to the same
    #       index...

    # Hash the given key and mod it by the capacity.
    # If the element in the array at that hash code is None, then:
    #     Increment the size.
    # Set the element in the array at that hash code to the given value.
    pass


def remove(dct, key):
    # Hash the given key and mod it by the capacity.
    # Set the element in the array at that hash code to None.
    # Decrement the size.
    # Return the removed value.
    pass
