"""
Module containing LinkedList class and Node class.
"""


class LinkedList():
    """
    Class to generate and modify linked list.
    """

    head = None

    def insert(self, data):
        """
        Method to create a node in the linked list with a .data value of *data*.
        """
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current._next:
                current = current._next

            current._next = node

    def includes(self, data):
        """
        Method to see if there is a node in the linked list with a .data value of *data*.
        """
        current = self.head
        while current._next:
            if current.data == data:
                return True

            current = current._next

    def print(self):
        """
        Method to print a string containing the .data value in every node.
        """
        output = ''
        current = self.head
        while current:
            if current == self.head:
                output += current.data
            else:
                output += ', ' + current.data
            current = current._next
        return output


class Node():
    def __init__(self, data):
        """
        Initializes an instance of a node with a .data value equal to *data*.
        """
        self.data = data
        self._next = None
