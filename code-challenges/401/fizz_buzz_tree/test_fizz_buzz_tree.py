from fizz_buzz_tree import fizz_buzz_tree, BinarySearchTree, BinaryTree


def test_exitst():
    """

    """
    assert fizz_buzz_tree


def test_replaces_3_with_fizz():
    """

    """
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(73)
    tree.add(3)
    tree.add(14)
    tree.add(6)
    tree.add(34)

    fizz_buzz_tree(tree)

    assert tree.root.data == 'Fizz'
