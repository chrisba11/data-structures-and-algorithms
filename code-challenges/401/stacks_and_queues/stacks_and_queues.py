from linked_list import LinkedList


class Node():
    """
    Class to create a new node.
    """
    def __init__(self, data):
        """
        Initializes an instance of a node with a *data* attribute value equal to *data*.
        """
        self.data = data
        self._next = None


class Stack():
    """
    Method to generate and modify a stack.
    """

    top = None

    def push(self, new_data):
        """
        Method to create a node at the top of a stack with a *data* attribute value equal to *new_data*.
        Returns *data* value.
        """
        new_node = Node(new_data)
        if self.top is None:
            self.top = new_node
        else:
            new_node._next = self.top
            self.top = new_node
        return self.top.data

    def pop(self):
        """
        Method to remove the top node from a stack and return the value of its *data* attribute.
        """
        if self.top is not None:
            current = self.top
            self.top = self.top._next
            current._next = None
            return current.data
        else:
            return 'Empty Stack'

    def peek(self):
        """
        Method to return the value of the *data* attribute from the top node of a stack.
        """
        if self.top is not None:
            return self.top.data
        else:
            return 'Empty Stack'


class Queue():
    """
    Method to generate and modify a new Queue.
    """

    front = None
    rear = None

    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        else:
            self.rear._next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is not None:
            current = self.front
            self.front = self.front._next
            current._next = None
            return current.data
        else:
            return 'Empty Queue'

    def peek(self):
        