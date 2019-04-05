class Graph:
    """

    """
    def __init__(self):
        self._graph = {}

    def add_vertex(self, data):
        vt = Vertex(data)
        self._graph[data] = {}





class Vertex:
    """
    Class to create a new vertex for a graph.
    """
    def __init__(self, data):
        """
        Initializes an instance of a vertex with a *data*
        attribute value equal to *data*.
        """
        self.data = data
        self.nxt = None
