from ..graph.graph import Graph
from ..stacks_and_queues.stacks_and_queues import Stack


class DepthFirstGraph(Graph):
    """
    Extends Graph class to add a method for depth_first
    traversal.
    """
    def depth_first(self, start_vertex):
        """
        Returns a list of vertices in the graph starting with
        the provided vertex and appending items by way of a
        pre-order depth-first traversal.
        """
        s = Stack()
        output = []

        if start_vertex in self._table:
            s.push(start_vertex)
            output.append(start_vertex)
            self._table[start_vertex]['visited'] = True

        def _traverse():
            """
            Traverses the graph in a depth-first way recursively
            while there are items in the stack.
            """
            while s.peek():
                curr = s.peek()
                for v in self._table[curr]['neighbors']:
                    if self._table[v]['visited'] is False:
                        s.push(v)
                        output.append(v)
                        self._table[v]['visited'] = True
                        _traverse()
                s.pop()

        _traverse()

        if self.get_vertices():
            for v in self.get_vertices():
                self._table[v]['visited'] = False

        return output
