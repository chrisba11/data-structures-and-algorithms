from ..graph.graph import Graph
from ..stacks_and_queues.stacks_and_queues import Queue


def breadth_first(graph, start_vertex):
    """
    Takes in a graph and a starting vertex and traverses
    the graph, returning a list of each vertex visited.
    """
    q = Queue()
    output = []

    if start_vertex in graph._table:
        q.nq(start_vertex)
        graph._table[start_vertex]['visited'] = True

    def _traverse(graph):
        """
        Dequeues a vertex and adds that vertex's neighbors to a
        queue and then appends that vertex to the output list.
        """
        nonlocal q
        nonlocal output

        curr = q.dq()
        if graph.get_neighbors(curr):
            for item in graph.get_neighbors(curr):

                if graph._table[item]['visited'] is False:
                    q.nq(item)
                    graph._table[item]['visited'] = True

        output.append(curr)

    while q.peek():
        _traverse(graph)

    if graph.get_vertices():
        for vertex in graph.get_vertices():
            graph._table[vertex]['visited'] = False

    return output
