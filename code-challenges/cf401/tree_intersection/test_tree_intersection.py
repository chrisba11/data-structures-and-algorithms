from ..tree.tree import BinarySearchTree
from ..hashtable.hashtable import Hashtable
from .tree_intersection import tree_intersection


def test_exists():
    assert tree_intersection


def test_currect_vals():
    bt1 = BinarySearchTree()
    bt2 = BinarySearchTree()

    bt1.add('A')
    bt1.add('B')
    bt1.add('C')
    bt1.add('D')
    bt1.add('E')

    bt2.add('A')
    bt2.add('C')
    bt2.add('E')

    assert tree_intersection(bt1, bt2) == ['A', 'C', 'E']


def test_currect_vals_two():
    bt1 = BinarySearchTree()
    bt2 = BinarySearchTree()

    bt1.add(1)
    bt1.add(2)
    bt1.add(3)
    bt1.add(4)

    bt2.add(4)

    assert tree_intersection(bt1, bt2) == [4]


def test_both_trees_empty():
    bt1 = BinarySearchTree()
    bt2 = BinarySearchTree()

    assert tree_intersection(bt1, bt2) == []
