class Graph:
    """

    """
    def __init__(self):
        self._table = {}

    def add_vertex(self, data):
        vt = Vertex(data)
        self._table[data] = {}

    def add_edge(self, vert_one, vert_two, weight=0):
        if vert_one in self._table and vert_two in self._table:
            self._table[vert_one][vert_two] = weight
            self._table[vert_two][vert_one] = weight
        elif vert_one not in self._table:
            raise AttributeError(vert_one + ' was not found in graph.')
        else:
            raise AttributeError(vert_two + ' was not found in graph.')

    def get_vertices(self):
        output = []
        for key in self._table:
            output.append(key)
        return output

    def get_neighbors(self, vertex):
        if vertex in self._table:
            return self._table[vertex]



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
