from fizz_buzz_tree import fizz_buzz_tree, BinarySearchTree, BinaryTree


def test_exitst():
    """
    Does the function exist.
    """
    assert fizz_buzz_tree


def test_replaces_3_with_fizz():
    """
    Does the function replace 3 with Fizz?
    """
    tree = BinarySearchTree()
    tree.add(3)

    fizz_buzz_tree(tree)

    assert tree.root.data == 'Fizz'


def test_replaces_10_with_buzz():
    """
    Does the function replace 10 with Buzz?
    """
    tree = BinarySearchTree()
    tree.add(3)
    tree.add(10)
    fizz_buzz_tree(tree)

    assert tree.root.right.data == 'Buzz'


def test_replaces_45_with_buzz():
    """
    Does the funtion replace 45 with Fizz-Buzz?
    """
    tree = BinarySearchTree()
    tree.add(16)
    tree.add(10)
    tree.add(23)
    tree.add(12)
    tree.add(45)
    fizz_buzz_tree(tree)

    assert tree.root.left.data == 'Buzz'
    assert tree.root.left.right.data == 'Fizz'
    assert tree.root.right.right.data == 'Fizz-Buzz'


def test_does_not_replace():
    """
    Does the funtion leave non-Fizz-Buzz values alone?
    """
    tree = BinarySearchTree()
    tree.add(16)
    tree.add(10)
    tree.add(23)
    tree.add(12)
    tree.add(45)
    fizz_buzz_tree(tree)

    assert tree.root.data == 16
    assert tree.root.right.data == 23
