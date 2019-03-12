class Node():
    """
    Class to create a node with tree-like attributes.
    """
    def __init__(self, data):
        """
        Initialize a node with data, left, and right attributes.
        """
        self.data = data
        self.left = None
        self.right = None
        self._next = None


class Queue():
    """
    Class to generate and modify a new Queue.
    """
    front = None
    rear = None

    def nq(self, node):
        """
        Method to add node at the *rear* of a queue.
        """
        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            self.rear._next = node
            self.rear = node

    def dq(self):
        """
        Method to remove a node from *front* of queue and return that node.
        """
        if self.front is not None:
            current = self.front
            self.front = self.front._next
            current._next = None
            if self.front is None:
                self.rear = None
            return current
        else:
            return None

    def peek(self):
        """
        Method to see if there is a node in a queue and if so, return it.
        """
        if self.front is not None:
            return self.front
        else:
            return None


class BinaryTree():
    """
    Class to create a binary tree.
    """
    def __init__(self):
        """
        Initialize a binary tree with a root attribute.
        """
        self.root = None

    def pre_order(self, curr=None):
        """
        Depth traversal method with order of Root, Left, Right.
        """
        output_array = []

        if not curr:
            curr = self.root

        output_array.append(curr.data)

        if curr.left:
            output_array += self.pre_order(curr.left)

        if curr.right:
            output_array += self.pre_order(curr.right)

        return output_array

    def in_order(self, curr=None):
        """
        Depth traversal method with order of Left, Node, Right.
        """
        output_array = []

        if not curr:
            curr = self.root

        if curr.left:
            output_array += self.in_order(curr.left)

        output_array.append(curr.data)

        if curr.right:
            output_array += self.in_order(curr.right)

        return output_array

    def post_order(self, curr=None):
        """
        Depth traversal method with order of Left, Right, Node.
        """
        output_array = []

        if not curr:
            curr = self.root

        if curr.left:
            output_array += self.post_order(curr.left)

        if curr.right:
            output_array += self.post_order(curr.right)

        output_array.append(curr.data)

        return output_array

    def breadth_first(self):
        """

        """
        q = Queue()
        x = []

        if self.root:
            q.nq(self.root)

        while q.peek():
            curr = q.dq()
            x.append(curr.data)
            if curr.left:
                q.nq(curr.left)
            if curr.right:
                q.nq(curr.right)

        return x


class BinarySearchTree(BinaryTree):
    """
    Class to create a binary search tree, extending BinaryTree.
    """
    def add(self, data, curr=None):
        """
        Method to add new node with data attribute = *data*.
        Will add left of current node if less than,
        and right of current node if greater than.
        """
        if not self.root:
            self.root = Node(data)
            return

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
                else:
                    self.add(data, curr.right)

    def contains(self, data, curr=None):
        """
        Method to see if *data* exists in any of the nodes in the tree.
        """
        if not self.root:
            return False

        if not curr:
            curr = self.root

        if data == curr.data:
            return True

        if data < curr.data:
            if curr.left:
                return self.contains(data, curr.left)

        if data > curr.data:
            if curr.right:
                return self.contains(data, curr.right)

        return False
