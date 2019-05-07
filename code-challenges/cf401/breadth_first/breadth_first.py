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

        while q.peek():
            curr = q.dq()
            if self.get_neighbors(curr):
                for item in self.get_neighbors(curr):

                    if self._table[item]['visited'] is False:
                        q.nq(item)
                        self._table[item]['visited'] = True

            output.append(curr)

        if self.get_vertices():
            for vertex in self.get_vertices():
                self._table[vertex]['visited'] = False

        return output
