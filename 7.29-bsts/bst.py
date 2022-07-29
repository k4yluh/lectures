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
    # NOTE: All BSTs are binary trees, and are therefore recursive:
    #         * The smallest BSTs have 0 or 1 nodes.
    #         * All larger BSTs have a root node and 1 or 2 smaller subtrees.
    #       ...BST operations can be performed recursively.

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
    #     NOTE: We have now inserted the key into the left subtree, and we
    #           have returned to the parent of that left subtree.
    #     Set the root's left child to the root of resulting left subtree.
    # Else, do:
    #     Recurse on the right subtree.
    #     Set the root's right child to the root of resulting right subtree.
    # (return the tree?)
    pass


def remove(bst, key):
    pass


def inorder(bst):
    pass
