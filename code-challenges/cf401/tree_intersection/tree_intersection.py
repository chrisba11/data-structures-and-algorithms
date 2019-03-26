from ..hashtable.hashtable import Hashtable


def tree_intersection(bt1, bt2):
    """

    """

    ht = Hashtable()
    match_arr = []

    def _tree_table(curr):
        """

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
