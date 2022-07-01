class List:
    """ An ordered collection of elements """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this list:
        self.size = 0


class Node:
    """ A single node in a linked list """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next


def get(lst, idx):
    # Set a current node reference to the head.
    # Set a counter to 0.
    # For counter from 0 to idx, do:
    #     Set the current node to the current node's next.
    # Return the current node's value.
    pass


def set(lst, idx, value):
    # Set a current node reference to the head.
    # Set a counter to 0.
    # For counter from 0 to idx, do:
    #     Set the current node to the current node's next.
    # Set the current node's value to the given value. 
    pass


def add(lst, idx, value):
    # If adding to the head:
    #     Make a new node
    #     Set the new node's next to the head -- this still works if the list
    #      was empty; it just makes the new node's next None, which is correct
    #     Set the head to that new node
    # Else if adding to the end of a non-empty list:
    #     Make a new node with no "next"
    #     Find the node *before* the desired index
    #     Set the previous node's next to the new node
    # Else if adding to the middle of a non-empty list:
    #     Make a new node
    #     Find the node *before* the desired index
    #     Set the new node's next to the previous node's next -- this *must*
    #      be done before changing the previous node's next, which is the only
    #      way to access the rest of the nodes
    #     Set the previous node's next to the new node
    pass


def remove(lst, idx):
    # ...
    # Else if removing from the middle of a non-empty list:
    #     Find the node *before* the desired index
    #     Get the previous node's next's next -- this is just the node *after*
    #      the desired index.
    #     Set the previous node's next to that successor node, thereby
    #      "unlinking" the removed node from the chain of nodes.
    pass
