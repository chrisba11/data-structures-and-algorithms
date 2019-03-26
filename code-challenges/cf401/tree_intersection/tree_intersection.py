from ..hashtable.hashtable import Hashtable


def tree_intersection(bt1, bt2):
    """
    Takes in 2 binary trees and returns a list of all matching values contained in the `data` property the tree nodes.
    """

    ht = Hashtable()
    match_arr = []

    def _tree_table(curr):
        """
        Takes in a node and adds it's `data` property as a key and value to a hash table.
        """
        if curr:
            if curr.data:
                ht.add(curr.data, curr.data)

            if curr.left:
                _tree_table(curr.left)

            if curr.right:
                _tree_table(curr.right)

    def _tree_check(curr):
        """
        Takes in a node and checks to see if the hash table has a key that matches the node's `data` property.
        """
        if curr:
            if ht.contains(curr.data):
                match_arr.append(curr.data)

            if curr.left:
                _tree_check(curr.left)

            if curr.right:
                _tree_check(curr.right)

    _tree_table(bt1.root)
    _tree_check(bt2.root)

    return match_arr
