from binary_tree import BinaryTree, TreeNode


def test_init():
    node_left = TreeNode(1)
    node_right = TreeNode(2)
    root = TreeNode(0, left=node_left, right=node_right)
    tree = BinaryTree(root)

    assert tree.root == root
    assert tree.root.left == node_left
    assert tree.root.right == node_right
