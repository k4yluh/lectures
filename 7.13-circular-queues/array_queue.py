class Queue:
    """ A FIFO collection of elements """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The index of the element at the front:
        self.front = -1
        # The index of the element at the back:
        self.back = -1


def enqueue(queue, value):
    # If the size is equal to the capacity:
    #     Create a new array with double the capacity.
    #     Copy the elements of the old array into the new array, "unwrapping"
    #      them as we go. Note that this is not inefficient; copying was
    #      already going to be O(n) anyways.
    # If the front and back are both -1 (the queue is empty):
    #     Set array[0] to the value.
    #     Set both the front and back to 0.
    # Else:
    #     Set the back to (back + 1) % capacity.
    #     Set array[back] to the value.


def dequeue(queue):
    # Set a temporary variable to array[front].
    # If front equals back:
    #     Set front and back to -1.
    # Else:
    #     Set the front to (front + 1) % capacity.
    # Return the temporary variable.


def peek(queue):
    # Return array[front].
