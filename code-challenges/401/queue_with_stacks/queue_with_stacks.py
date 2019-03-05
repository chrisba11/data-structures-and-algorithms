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
    empty = 'Empty Stack'

    def push(self, new_data):
        """
        Method to add a new node at the top of a stack with a *data* attribute value equal to *new_data*.
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
            return self.empty

    def peek(self):
        """
        Method to return the value of the *data* attribute from the top node of a stack.
        """
        if self.top is not None:
            return self.top.data
        else:
            return self.empty


class Queue():
    """

    """
    def __init__(self):
        """

        """
        stack_one = Stack()
        stack_two = Stack()

    def enqueue(self, data):
        """

        """
        stack_one.push(data)

    def dequeue(self):
        """

        """
        if stack_two.peek() != 'Empty Stack':
            return stack_two.pop().data
        elif stack_one.peek() != 'Empty Stack':
            while stack_one.peek() != 'Empty Stack':
                stack_two.push(stack_one.pop().data)
            return stack_two.pop().data
        else:
            return 'Empty Queue'
