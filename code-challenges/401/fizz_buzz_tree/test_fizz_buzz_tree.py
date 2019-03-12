from fizz_buzz_tree import fizz_buzz_tree, BinarySearchTree, BinaryTree


def test_exitst():
    """

    """
    assert fizz_buzz_tree


def test_replaces_3_with_fizz():
    """

    """
    tree = BinarySearchTree()
    tree.add(3)

    fizz_buzz_tree(tree)

    assert tree.root.data == 'Fizz'


def test_replaces_10_with_buzz():
    """

    """
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(10)
    fizz_buzz_tree(tree)

    assert tree.root.right.data == 'Buzz'
