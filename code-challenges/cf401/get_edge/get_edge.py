from ..graph.graph import Graph


def get_edge(graph, list):
    price = 0

    if len(list) < 2:
        return (False, 0)

    for i in range(1, len(list)-1):
        neighbors_of_previous = graph.get_neighbors(list[i-1])
        current = list[i]

        if current in neighbors_of_previous:
            price += neighbors_of_previous[current]
        else:
            return (False, 0)

    return (True, price)
