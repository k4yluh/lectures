class PriorityQueue:
    """ A prioritized collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array, placeholder at index 0:
        # NOTE: To make the indexing math work out nicely, there can't be any
        #       "nodes" at index 0.
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this queue:
        self.size = 0


# NOTE: The array represents a complete binary tree in which every node is
#       larger than its children: a "binary heap".


def enqueue(pqueue, value):
    pass


def dequeue(pqueue):
    pass


def peek(pqueue):
    # Return the root (whose index is always 1).
    pass
