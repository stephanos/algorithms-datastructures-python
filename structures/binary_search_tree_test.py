from binary_search_tree import BinarySearchTree, TreeNode


def test_init():
    tree = BinarySearchTree(50)
    assert tree.root == TreeNode(50)

def test_insert():
    tree = BinarySearchTree(50)
    tree.insert(25)
    assert tree.root == TreeNode(50, left=TreeNode(25))

    tree.insert(75)
    assert tree.root == TreeNode(50, left=TreeNode(25), right=TreeNode(75))

    tree.insert(100)
    assert tree.root == TreeNode(50, left=TreeNode(25), \
                                     right=TreeNode(75, right=TreeNode(100)))

    tree.insert(0)
    assert tree.root == TreeNode(50, left=TreeNode(25, left=TreeNode(0)), \
                                     right=TreeNode(75, right=TreeNode(100)))

def test_search():
    tree = BinarySearchTree(50)
    for i in range(0, 110, 10):
        tree.insert(i)

    assert tree.search(tree.root, 50)
    assert tree.search(tree.root, 20)
    assert not tree.search(tree.root, 99)

def test_minimum():
    tree = BinarySearchTree(50)
    for i in range(0, 110, 10):
        tree.insert(i)

    assert tree.minimum() == 0

def test_maximum():
    tree = BinarySearchTree(50)
    for i in range(0, 110, 10):
        tree.insert(i)

    assert tree.maximum() == 100
