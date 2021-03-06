class Graph:
    """
    Class to create graph instances.
    """
    def __init__(self):
        """
        Instantiates each graph instance with a table dictionary.
        """
        self._table = {}

    def add_vertex(self, data):
        """
        Method to add a vertex (node) to a graph with the
        *data* attribute equal to the argument supplied.
        """
        self._table[data] = {'visited': False, 'neighbors': {}}

    def add_edge(self, vert_one, vert_two, weight=0):
        """
        Adds an edge between two supplied vertices.
        """
        if vert_one in self._table and vert_two in self._table:
            self._table[vert_one]['neighbors'][vert_two] = weight
            self._table[vert_two]['neighbors'][vert_one] = weight
        else:
            return None

    def get_vertices(self):
        """
        Returns a list of vertices found in a graph.
        Returns None if graph is empty.
        """
        output = []
        for key in self._table:
            output.append(key)
        if output == []:
            return None
        return output

    def get_neighbors(self, vertex):
        """
        Returns a dictionary of neighbors for the given vertex.
        Neighbors will be the keys and weights will be the values.
        """
        if vertex in self._table:
            return self._table[vertex]['neighbors']
        else:
            return None

    def size(self):
        """
        Returns the number of vertices in the graph.
        """
        return len(self._table)


class Vertex:
    """
    Class to create a new vertex for a graph.
    """
    def __init__(self, data):
        """
        Initializes an instance of a vertex with a *data*
        attribute value equal to the argument passed in.
        """
        self.data = data
