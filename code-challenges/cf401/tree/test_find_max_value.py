from tree import BinarySearchTree, BinaryTree


def test_exists():
    tree = BinarySearchTree
    assert tree.find_maximum_value


def test_max_value_is_57():
    tree = BinarySearchTree()
    tree.add(43)
    tree.add(13)
    tree.add(12)
    tree.add(40)
    tree.add(57)

    assert tree.find_maximum_value() == 57


def test_max_val_changes():
    tree = BinarySearchTree()
    tree.add(43)
    assert tree.find_maximum_value() == 43
    tree.add(13)
    tree.add(57)
    assert tree.find_maximum_value() == 57
    tree.add(12)
    tree.add(80)
    assert tree.find_maximum_value() == 80
    tree.add(40)

    assert tree.find_maximum_value() == 80


def test_max_val_is_int():
    tree = BinarySearchTree()
    tree.add(12)
    tree.add(60)
    tree.add(57)

    assert isinstance(tree.find_maximum_value(), int)


def test_empty_tree():
    tree = BinarySearchTree()

    assert tree.find_maximum_value() == 0
