class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next, previous):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next
        # The previous node in the linked list:
        self.previous = previous


def get(lst, idx):
    # NOTE: This seems clever, but at the end of the day, n/2 is still O(n)...
    # If the index is in the first half:
    #     Start from the head and "walk forwards"...
    # Else:
    #     Start from the tail and "walk backwards"...
    pass


def set(lst, idx, value):
    pass


def add(lst, idx, value):
    # If adding to an empty list:
    #     Make a new node with no "previous" or "next"
    #     Set the head to that new node
    #     Set the tail to that new node
    # Else if adding to the head:
    #     Make a new node with no "previous"
    #     Set the new node's next to the head -- this still works if the list
    #      was empty; it just makes the new node's next None, which is correct
    #     Set the head's previous to the new node
    #     Set the head to that new node
    # Else if adding to the tail of a non-empty list:
    #     Make a new node with no "next"
    #     Set the new node's previous to the tail
    #     Set the tail's next to the new node
    #     Set the tail to that new node
    # Else if adding to the middle of a non-empty list:
    #     ...
    pass


def remove(lst, idx):
    pass
