class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this queue:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next
        # NOTE: It is not incorrect to make this a doubly linked list, but
        #       it should be possible to get away with a singly linked list,
        #       since we don't plan to traverse the list, and there is no
        #       reason to overcomplicate the problem.


def enqueue(queue, value):
    # If the queue is empty:
    #     Create a new node with no next.
    #     Set the node's value to the given value.
    #     Set the head and the tail to the new node.
    # Else:
    #     Create a new node with no next.
    #     Set the node's value to the given value.
    #     Set the tail's next to the new node.
    #     Set the tail to the new node.
    # Increment the size.


def dequeue(queue):
    # If the queue is of size 1:
    #     Set a temporary variable to that one node's value.
    #     Set the head and the tail to None.
    # Else:
    #     Set a temporary variable to the head's value.
    #     Set the head to the head's next.
    # Decrement the size.
    # Return the temporary variable.


def peek(queue):
    # Return the head's value.
