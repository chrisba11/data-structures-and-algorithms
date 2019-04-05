"""
Module containing LinkedList class and Node class.
"""


class LinkedList():
    """
    Class to generate and modify linked list.
    """
    def __init__(self, arg=None):
        self.head = None
        if arg is not None:
            if hasattr(arg, '__iter__') and not isinstance(arg, str):
                for i in arg:
                    self.append(i)
            else:
                self.append(arg)

    def insert(self, new_data):
        """
        Method to create a node in the linked list with a .data value
        of *new_data* at the beginning of the list.
        """
        node = Node(new_data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            self.head = node
            self.head.nxt = current

    def includes(self, lookup):
        """
        Method to see if there is a node in the linked list with
        a .data value of *lookup*.
        """
        current = self.head
        try:
            while current.nxt:
                if current.data == lookup:
                    print('included!')
                    return True
                else:
                    current = current.nxt
            if current.data == lookup:
                print('included!')
                return True
        except:
            print('no .nxt')

    def print(self):
        """
        Method to print a string containing the
        .data value in every node.
        """
        output = ''
        current = self.head
        while current:
            if current == self.head:
                output += current.data
            else:
                output += ', ' + current.data
            current = current.nxt
        return output

    def append(self, new_data):
        """
        Method to create a node in the linked list with a
        .data value of *new_data* at the end of the list.
        """
        node = Node(new_data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.nxt:
                current = current.nxt
            current.nxt = node

    def add_before(self, lookup, new_data):
        """
        Method to create a node in the linked list with a .data
        value of *new_data* before the node with the .data
        value of *lookup* in the list.
        """
        node = Node(new_data)
        if self.includes(lookup):
            if self.head.data == lookup:
                self.insert(new_data)
            else:
                current = self.head
                while current.nxt.data != lookup:
                    current = current.nxt
                node.nxt = current.nxt
                current.nxt = node
        else:
            print('Lookup data not found in list.')

    def add_after(self, lookup, new_data):
        """
        Method to create a node in the linked list with a .data value
        of *new_data* after the node with the .data
        value of *lookup* in the list.
        """
        node = Node(new_data)
        if self.includes(lookup):
            current = self.head
            while current.data != lookup:
                current = current.nxt
            node.nxt = current.nxt
            current.nxt = node
        else:
            print('Lookup data not found in list.')

    def k_from_end(self, k):
        """
        Method to return the data of the kth node in a linked list.
        """
        total_nodes = 0
        position = 0
        current = self.head
        while current and current.nxt:
            total_nodes += 1
            current = current.nxt
        if current and not current.nxt:
            total_nodes += 1
        else:
            return 'Empty Linked List'
        if k < total_nodes:
            position = total_nodes - k
        else:
            return 'Exception'
        current = self.head
        for i in range(1, position):
            current = current.nxt
        return current.data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.nxt

    def __next__(self):
        current = self.head
        if current:
            yield current.nxt

    def __add__(self, val):
        output = LinkedList()

        for i in self:
            output.append(i)

        if hasattr(val, '__iter__') and not isinstance(val, str):
            for i in val:
                output.append(i)
        else:
            output.append(val)

        return output

    def __iadd__(self, val):
        if hasattr(val, '__iter__') and not isinstance(val, str):
            for i in val:
                self.append(i)
        else:
            self.append(val)

        return self


class Node():
    def __init__(self, data):
        """
        Initializes an instance of a node with a
        .data value equal to *data*.
        """
        self.data = data
        self.nxt = None
