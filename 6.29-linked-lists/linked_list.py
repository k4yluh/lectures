# Implements a linked list.
# CSC 202, Lab 2
# Given code, Summer '19


class List:
    """
    An ordered collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        return (type(other) == List
                and self.head == other.head
                and self.size == other.size)

    def __repr__(self):
        return "List(%r, %d)" % (self.head, self.size)


class Node:
    """
    A single node in a linked list
    NOTE: Do not alter this class.
    """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next

    def __eq__(self, other):
        return (type(other) == Node
                and self.value == other.value
                and self.next == other.next)

    def __repr__(self):
        return "Node(%r, %r)" % (self.value, self.next)


def size(lst):
    """
    Count the number of elements in a list.
    TODO: Implement this function. It must have O(1) complexity.
    :param lst: A List
    :return: The number of elements in the list
    """
    count = 0
    for e in range(lst.size):
        count += 1
    return count


def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function. It must have O(n) complexity.
    :param lst: A List
    :param idx: An index at which to get an element
    :return: The element in the list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx > lst.size:
        raise IndexError

    cur = lst.head
    for i in range(idx):
        cur = cur.next
    return cur.value


def set(lst, idx, value):
    """
    Set the element at an index.
    TODO: Implement this function. It must have O(n) complexity.
    :param lst: A List
    :param idx: An index at which to set an element
    :param value: A value to which to set an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx > lst.size - 1:
        raise IndexError

    cur_n = lst.head
    for i in range(idx):
        cur_n = cur_n.next
    cur_n.value = value


def add(lst, idx, value):
    """
    Add an element at an index.
    TODO: Implement this function. It must have O(n) complexity.
    :param lst: A List
    :param idx: An index at which to add an element
    :param value: A value to add as an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx > lst.size:
        raise IndexError

    if idx == 0:
        new = Node(value, lst.head)
        lst.head = new
    elif idx == lst.size and lst.size > 0:
        new = Node(value, None)
        prev = lst.head
        for i in range(idx - 1):
            prev = prev.next
        prev.next = new
    elif 0 < idx < lst.size:
        new = Node(value, None)
        prev = lst.head
        for i in range(idx - 1):
            prev = prev.next
        new.next = prev.next
        prev.next = new
    lst.size += 1


def remove(lst, idx):
    """
    Remove the element at an index.
    TODO: Implement this function. It must have O(n) complexity.
    :param lst: A List
    :param idx: An index at which to remove an element
    :raise IndexError: If the index is out-of-bounds
    :return: The removed element
    """
    if idx < 0 or idx > lst.size - 1:
        raise IndexError
    removed = 0
    if idx == 0:
        removed = lst.head
        lst.head = lst.head.next
    elif 0 < idx < lst.size - 1:
        prev = lst.head
        aft = lst.head
        for i in range(idx - 1):
            prev = prev.next
        removed = prev.next.next
        for i in range(idx + 1):
            aft = aft.next
        prev.next = aft
    elif idx == lst.size and lst.size > 0:
        cur = lst.head
        for i in range(idx):
            cur = cur.next
        removed = cur.value
        cur.value = None
    lst.size -= 1
    return removed
