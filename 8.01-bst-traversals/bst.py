class BinarySearchTree:
    """ A binary search tree """

    def __init__(self):
        # The root of this tree:
        self.root = None
        # The number of nodes in this tree:
        self.size = 0


class Node:
    """ A single node in a binary search tree """

    def __init__(self, key, left, right):
        # The key contained in this node:
        self.key = key
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def find(bst, key):
    # If the tree is empty, then:
    #     Bad job! :(
    # Else if the root's key equals the given key, then:
    #     Good job! :)
    # Else if the root's key is too large, then:
    #     Recurse on the left subtree.
    # Else, do:
    #     Recurse on the right subtree.
    pass


def insert(bst, key):
    # If the tree is empty, then:
    #     Make a new node to contain the given key.
    #     Set the tree's root to the new node.
    #     Increment the size.
    # Else if the root's key equals the given key, then:
    #     Good job! :)
    # Else if the root's key is too large, then:
    #     Recurse on the left subtree.
    #     Set the root's left child to the root of resulting left subtree.
    # Else, do:
    #     Recurse on the right subtree.
    #     Set the root's right child to the root of resulting right subtree.
    pass


def remove(bst, key):
    # If the tree is empty, then:
    #     Bad job! :(
    # Else if the root's key equals the given key, then:
    #     If the root does not have a right child, then:
    #         Replace the root with its left child.
    #         Decrement the size.
    #     Else if the root does not have a left child, then:
    #         Replace the root with its right child.
    #         Decrement the size.
    #     Else, do:
    #         NOTE: The smallest key in the right subtree must be:
    #                 * Smaller than any other to the right (by construction)
    #                 * Larger than any to the left (by definition of a BST)
    #                 * Something without a left (else that child is smaller)
    #               ...that smallest key can take our place.
    #         Find the smallest key starting from the right child.
    #         Recursively remove that smallest key from the right subtree.
    #         Set the root's key to that smallest key.
    # Else if the root's key is too large, then:
    #     Recurse on the left subtree.
    #     Set the root's left child to the root of resulting left subtree.
    # Else, do:
    #     Recurse on the right subtree.
    #     Set the root's right child to the root of resulting right subtree.
    pass


def min(bst):
    # If the root has no left child, then:
    #     Return the root's key.
    # Else, do:
    #     Recurse on the left subtree.
    pass


def inorder(bst):
    # If the root of the given tree does not exist, then:
    #     Return (whatever you were asked to return).
    # Else if the root has no children, then:
    #     Mark the root as "explored" (do whatever you came here to do).
    #     Return.
    # Else, do:
    #     NOTE: The keys to the left, by def'n, must be smaller than the root's
    #           key, thus, the left subtree must be explored first.
    #     Recurse on the left subtree.
    #     Mark the root as "explored".
    #     Recurse on the right subtree.
    #     Return.
    pass
