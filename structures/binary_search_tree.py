class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value and \
                self.left == other.left and \
                self.right == other.right
        else:
            return False

    def __str__(self):
        return 'Tree ({}, {}, {})'.format(self.value, self.left, self.right)


class BinarySearchTree():

    def __init__(self, value):
        self.root = TreeNode(value)

    def insert(self, item):
        node = self.root
        while node is not None:
            if item < node.value:
                if node.left is None:
                    node.left = TreeNode(item)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(item)
                    return
                else:
                    node = node.right

    def search(self, node, item):
        if node is None:
            return False
        else:
            if node.value == item:
                return True
            elif node.value < item:
                return self.search(node.right, item)
            else:
                return self.search(node.left, item)

    def minimum(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.value

    def maximum(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value
