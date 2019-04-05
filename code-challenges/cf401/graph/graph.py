class Graph:
    """

    """
    def __init__(self):
        self._table = {}

    def add_vertex(self, data):
        vt = Vertex(data)
        self._table[data] = {}

    def add_edge(self, vert_one, vert_two, weight=0):
        self._table[vert_one][vert_two] = weight
        self._table[vert_two][vert_one] = weight



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
