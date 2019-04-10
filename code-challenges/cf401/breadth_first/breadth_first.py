from ..graph.graph import Graph
from ..stacks_and_queues import Queue


def breadth_first(graph, start_vertex):
    q = Queue()
    output = []
    q.nq(start_vertex)
    graph._table[start_vertex]['visited'] = True

    def traverse(graph):
        """

        """
        nonlocal q
        nonlocal output

        curr = q.dq()
        for item in graph.get_neighbors(curr):
            if graph._table[item]['visited'] = False:
                q.nq(item)
                graph._table[item]['visited'] = True
            output.append(curr)
            graph._table[curr]['visited'] = False

        while q.peek():
            _traverse(graph)

        return output

