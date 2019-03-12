from tree import BinaryTree, BinarySearchTree, Node, Queue


def test_exists():
    tree = BinarySearchTree()
    assert tree.breadth_first() == []


def test_reads_one():
    tree = BinarySearchTree()
    tree.add(67)
    assert tree.breadth_first() == [67]


def test_reads_four():
    tree = BinarySearchTree()
    tree.add(67)
    tree.add(62)
    tree.add(65)
    tree.add(90)
    assert tree.root.data == 67
    assert tree.root.left.data == 62
    assert tree.root.right.data == 90
    assert tree.breadth_first() == [67, 62, 90, 65]
