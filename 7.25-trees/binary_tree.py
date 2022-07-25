class BinaryTree:
    """ A binary tree """

    def __init__(self, value = None):
        if value is None:
            # The root of this empty tree:
            self.root = None
            # The number of nodes in this tree:
            self.size = 0
        else:
            # The root of this singleton tree:
            self.root = Node(value, None, None)
            # The number of nodes in this tree:
            self.size = 1


class Node:
    """ A single node in a binary tree """

    def __init__(self, value, left, right):
        # The value contained in this node:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right


def combine(value, left, right):
    # Make a new tree whose root node contains the given value.
    # Set the root's left child to the root of the given left tree.
    # Set the root's right child to the root of the given right tree.
    # Set the new tree's size to size of left + size of right + 1.
    # Return the new tree.
    pass


def preorder(tree):
    # NOTE: Binary trees are recursively defined structures:
    #         * Base case: The smallest possible tree has 0 or 1 nodes.
    #         * Recursive case: All other trees can be constructed by
    #           combining two smaller trees as the children of a new root.
    #       ...binary trees can be traversed by recursive functions.

    # If the root of the given tree does not exist, then:
    #     Return (whatever you were asked to return).
    # Else if the root has no children, then:
    #     Mark the root as "explored" (do whatever you came here to do).
    #     Return.
    # Else, do:
    #     Mark the root as "explored".
    #     Recurse on the left subtree.
    #     Recurse on the right subtree.
    #     Return.
    pass


def postorder(tree):
    pass


def levelorder(tree):
    pass
