from ..graph.graph import Graph


def get_edge(graph, input_list):
    price = 0

    if len(input_list) < 2:
        return (False, 0)

    for i in range(1, len(input_list)):
        neighbors_of_previous = graph.get_neighbors(input_list[i-1])
        current = input_list[i]

        if current in neighbors_of_previous:
            price += neighbors_of_previous[current]
        else:
            return (False, 0)

    return (True, price)
