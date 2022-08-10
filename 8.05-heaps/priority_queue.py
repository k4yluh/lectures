# Implements a priority queue.
# CSC 202, Lab 8
# Given code, Summer '19


# import pwd


class PriorityQueue:
    """
    A prioritized collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array, placeholder at index 0:
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this queue:
        self.size = 0

    def __eq__(self, other):
        if type(other) != PriorityQueue or self.size != other.size:
            return False

        for idx in range(1, self.size + 1):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "PriorityQueue(%d, %r, %d)"\
               % (self.capacity, self.array, self.size)


def size(pqueue):
    """
    Calculate the size of a priority queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param pqueue: A PriorityQueue
    :return: The number of elements in the priority queue
    """
    return pqueue.size


def enqueue(pqueue, value):
    """
    Enqueue an element with some priority to a priority queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param pqueue: A PriorityQueue
    :param value: A comparable value to be enqueued
    """
    if pqueue.size == pqueue.capacity:
        pqueue.capacity *= 2
        temp = pqueue.array
        pqueue.array = [None] * (pqueue.capacity+1)
        for i in range(pqueue.size):
            pqueue.array[i] = temp[i]
    pqueue.array[pqueue.size + 1] = value
    while value != pqueue.array[1] and value > pqueue.array[(pqueue.size + 1)//2]:
        temp = pqueue.array[(pqueue.size + 1)//2]
        pqueue.array[(pqueue.size + 1)//2] = value
        value = temp
    pqueue.size += 1


def dequeue(pqueue):
    """
    Dequeue the element of highest priority from a priority queue.
    TODO: Implement this function. It must have O(log n) complexity.

    :param pqueue: A PriorityQueue
    :return: The dequeued element
    :raise ValueError: If the priority queue is empty
    """
    if pqueue.size == 0:
        raise ValueError
    pqueue.array[1] = pqueue.array[pqueue.size]
    cur = 1
    while pqueue.array[cur] < pqueue.array[(2*cur)] and pqueue.array[cur] < pqueue.array[(2*cur+1)]:
        if pqueue.array[2*cur] > pqueue.array[2*cur+1] and pqueue.array[2*cur] > pqueue.array[cur]:
            temp = pqueue.array[2*cur]
            pqueue.array[2*cur] = pqueue.array[cur]
            pqueue.array[cur] = temp
        elif pqueue.array[(2*cur+1)] > pqueue.array[cur]:
            temp = pqueue.array[(2*cur+1)]
            pqueue.array[(2*cur+1)] = pqueue.array[cur]
            pqueue.array[cur] = temp
    pqueue.size -= 1
    return temp 


def peek(pqueue):
    """
    Peek at the element of highest priority in a queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param pqueue: A PriorityQueue
    :return: The peeked element
    :raise ValueError: If the priority queue is empty
    """
    if pqueue.size == 0:
        raise ValueError
    else:
        return pqueue.array[1]
        
