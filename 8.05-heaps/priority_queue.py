class PriorityQueue:
    """ A prioritized collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array, placeholder at index 0:
        # NOTE: Complete binary trees can be stored in arrays, where:
        #         * The "root" is always index 1.
        #         * The "parent" of index i is index i // 2.
        #         * The "children" of index i are indices 2i and 2i + 1.
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this queue:
        self.size = 0


def enqueue(pqueue, value):
    # NOTE: Elements must always be added at the next leaf. Since the tree
    #       is complete, the next leaf is always index size + 1.
    # NOTE: The maximum number of swaps is the height of the tree -- this
    #       loop will never run more than O(log n) times. However, *most* of
    #       the nodes in this tree are leaves. Most elements require only
    #       one or two swaps, because they are already close to where they
    #       need to be.

    # If the array is at capacity:
    #     Double the capacity.
    #     Create a new array with new capacity + 1.
    #     Copy the elements of the old array into the new array.
    # Set the next leaf (index size + 1) to the given value.
    # While the value is bigger than its parent (index current // 2), then:
    #     Swap the value with its parent.
    # Increment the size.
    pass


def dequeue(pqueue):
    # NOTE: Nodes must always be removed from the last leaf. Since the tree
    #       is complete, the last leaf is always index size.
    # NOTE: The maximum number of swaps is the height of the tree -- this
    #       loop will never run more than O(log n) times. However, *most* of
    #       the nodes in this tree are leaves. Most elements require almost
    #       all of the swaps, because they are moved into the root, which is
    #       far from where they need to be.

    # Set the root (index 1) to the last leaf (index size).
    # While the current has children larger than itself, do:
    #     If the left child (index 2i) is bigger than the right child
    #      (index 2i + 1) and bigger than the current, then:
    #         Swap the current with its left child.
    #     Else if the right child is bigger than the current, then:
    #         Swap the current with its right child.
    # Decrement the size.
    # Return the old root.
    pass


def peek(pqueue):
    # Return the root (index 1).
    pass
