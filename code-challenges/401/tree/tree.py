class Node():
    """

    """
    def __init__(self, data):
        """

        """
        self.data = data
        self.left = None
        self.right = None


class BinaryTree():
    """

    """
    def __init__(self):
        """

        """
        self.root = None

    def pre_order(self, node):
        """
        Depth traversal method with order of Root, Left, Right.
        """
        output_array = []

        output_array.append(node.data)

        if node.left:
            output_array += pre_order(node.left)

        if node.right:
            output_array += pre_order(node.right)

        return output_array

    def in_order(self, node):
        """

        """
        output_array = []

        if node.left:
            output_array += in_order(node.left)

        output_array.append(node.data)

        if node.right:
            output_array += in_order(node.right)

        return output_array

    def post_order(self, node):
        """

        """
        output_array = []

        if node.left:
            output_array += post_order(node.left)

        output_array.append(node.data)

        if node.right:
            output_array += post_order(node.right)

        return output_array


class BinarySearchTree():
    """

    """
    def add(self, data, curr=None):
        """

        """
        if not self.root:
            self.root = Node(data)

        if curr is None:
            curr = self.root
        
        if curr:
            if data < curr.data:
                if not curr.left:
                    curr.left = Node(data)
                else:
                    self.add(data, curr.left)

            if data >= curr.data:
                if not curr.right:
                    curr.right = Node(data)
                else: self.add(data, curr.right)

    def contains(self, data, curr=None):
        """

        """
        if not self.root:
            return False

        if not curr:
            curr = self.root

        if data == curr.data:
            return True

        if curr.left:
            self.contains(data, curr.left)

        if curr.right:
            self.contains(data, curr.right)

        return False
