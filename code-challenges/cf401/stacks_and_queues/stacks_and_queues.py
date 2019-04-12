class Node():
    """
    Class to create a new node.
    """
    def __init__(self, data):
        """
        Initializes an instance of a node with a *data*
        attribute value equal to *data*.
        """
        self.data = data
        self.nxt = None


class Stack():
    """
    Method to generate and modify a stack.
    """

    top = None

    def push(self, new_data):
        """
        Method to add a new node at the top of a stack with a
        *data* attribute value equal to *new_data*.
        Returns *data* value.
        """
        new_node = Node(new_data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.nxt = self.top
            self.top = new_node
        return self.top.data

    def pop(self):
        """
        Method to remove the top node from a stack and return
        the value of its *data* attribute.
        """
        if self.top is not None:
            current = self.top
            self.top = self.top.nxt
            current.nxt = None
            return current.data
        else:
            return None

    def peek(self):
        """
        Method to return the value of the *data* attribute from
        the top node of a stack.
        """
        if self.top is not None:
            return self.top.data
        else:
            return None


class Queue():
    """
    Class to generate and modify a new Queue.
    """
    front = None
    rear = None

    def nq(self, new_data):
        """
        Method to add node at the *rear* of a queue.
        """
        new_node = Node(new_data)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear.nxt = new_node
            self.rear = new_node

    def dq(self):
        """
        Method to remove a node from *front* of queue and
        return that node.
        """
        if self.front is not None:
            current = self.front
            self.front = self.front.nxt
            current.nxt = None
            if self.front is None:
                self.rear = None
            return current.data
        else:
            return None

    def peek(self):
        """
        Method to see if there is a node in a queue and if so,
        return it.
        """
        if self.front is not None:
            return self.front.data
        else:
            return None

    def __iter__(self):
        current = self.front
        while current:
            yield current.data
            current = current.nxt

    def __repr__(self):
        return f'<REPR: Queue Object with {self.front} at the front>'

    def __str__(self):
        return f'''Queue with {self.front} at the front and
                {self.rear} at the rear.'''
