class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this stack:
        self.size = 0


def push(stack, value):
    # If the size is equal to the capacity:
    #     Double the capacity.
    #     Create a new array with that new capacity.
    #     For i from 0 to the size of the list:
    #         Set new_array[i] to array[i].
    #     Set the list's array to that new array.
    # Set array[size] to the given value.
    # Increment the size.
    pass


def pop(stack):
    # Return array[size - 1].
    # Decrement the size.
    pass


def peek(stack);
    # Return array[size - 1].
    pass
