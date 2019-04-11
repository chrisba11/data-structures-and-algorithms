from ..graph.graph import Graph
from ..stacks_and_queues.stacks_and_queues import Queue


class BreadthFirstGraph(Graph):
    """
    Extends Graph class to include a breadth first traversal
    method.
    """

    def breadth_first(self, start_vertex):
        """
        Takes in a graph and a starting vertex and traverses
        the graph, returning a list of each vertex visited.
        """
        q = Queue()
        output = []

        if start_vertex in self._table:
            q.nq(start_vertex)
            self._table[start_vertex]['visited'] = True

        def _traverse(self):
            """
            Dequeues a vertex and adds that vertex's neighbors to a
            queue and then appends that vertex to the output list.
            """
            nonlocal q
            nonlocal output

            curr = q.dq()
            if self.get_neighbors(curr):
                for item in self.get_neighbors(curr):

                    if self._table[item]['visited'] is False:
                        q.nq(item)
                        self._table[item]['visited'] = True

            output.append(curr)

        while q.peek():
            _traverse(self)

        if self.get_vertices():
            for vertex in self.get_vertices():
                self._table[vertex]['visited'] = False

        return output
