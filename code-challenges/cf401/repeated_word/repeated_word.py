from tree.tree import BinarySearchTree, Node


def repeated_word(str):
    """
    Takes in a string and returns the first repeated word in the string.
    If there are no repeated words, it will return False.
    """
    tree = BinarySearchTree()
    arr = str.split(' ')
    root_node = Node(arr[0])
    tree.root = root_node
    curr = tree.root

    def _check(tree_node, new_node):
        """
        Private function to check if new node's value is equal to any nodes in the BST.
        If it matches, it will return that value. If it doesn't match, it will add the node to the tree.
        """

        if new_node.data == tree_node.data:
            return new_node.data

        if new_node.data < tree_node.data:
            if not tree_node.left:
                tree_node.left = new_node
            else:
                return _check(tree_node.left, new_node)

        if new_node.data > tree_node.data:
            if not tree_node.right:
                tree_node.right = new_node
            else:
                return _check(tree_node.right, new_node)

        return False

    result = False

    for i in range(1, len(arr)):
        node = Node(arr[i])
        result = _check(curr, node)
        if result is not False:
            break

    return result
