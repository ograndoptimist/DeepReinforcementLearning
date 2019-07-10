"""
    Structures needed to construct the brute force algorithm.
"""


class Node(object):
    """
        The baseline structure to build a Binary Search Tree.
    """
    def __init__(self):
        self.left = None
        self.right = None
        self.table_configuration = None


class BST(object):
    """
        A Binary Search Tree implementation.
    """
    def __init__(self):
        self.root = Node()
        self.n = 0

    def insert_item(self, item):
        pass

    def search_item(self, item):
        pass
