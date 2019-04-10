from ..graph.graph import Graph


def get_edge(graph, input_list):
    """
    Takes in a graph and a list. Determines whether a path is
    possible from the first element in the list through the last
    element in the list moving through each element in order
    from left to right. If there are edges connecting each
    element along the way, it will return a tuple of
    (True, total_of_edges_along_path). If one of the elements
    is not a neighbor of it's previous element, it will return
    (False, 0). If the input list is less than 2 elements, it
    will return (False, 0).
    """
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
