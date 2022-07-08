class Stack:
    """ A LIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this stack:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def push(stack, value):
    # If the stack is empty:
    #     Create a new node with no next.
    #     Set the new node's value to the given value.
    #     Set the head to that new node.
    # Else:
    #     Create a new node whose next is the old head.
    #     Set the new node's value to the given value.
    #     Set the head to that new node.
    # Increment the size.
    pass


def pop(stack):
    # Save the head's value in a temporary variable.
    # Set the head to the head's next.
    # Return the temporary variable.
    # Decrement the size.
    pass


def peek(stack):
    # Return the head's value.
    pass
