# Graph
Graph class to hold vertices and edges with weights.

## Challenge
- Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

    - `AddNode()`
        - Adds a new node to the graph
        - Takes in the value of that node
        - Returns the added node

    - `AddEdge()`
        - Adds a new edge between two nodes in the graph
        - Include the ability to have a “weight”
        - Takes in the two nodes to be connected by the edge
        - Both nodes should already be in the Graph

    - `GetNodes()`
        - Returns all of the nodes in the graph as a collection (set, list, or similar)

    - `GetNeighbors()`
        - Returns a collection of nodes connected to the given node
        - Takes in a given node
        - Include the weight of the connection in the returned collection

    - `Size()`
        - Returns the total number of nodes in the graph

## Approach
- `add_vertex(self, data)`
    - I create a new vertex (node) with a *data* attribute matching the input value.
    - I add the node to the graph's table dictionary with its *data* as the key and an empty dictionary as that key's value.

- `add_edge(self, vert_one, vert_two, weight=0)`
    - If both of the supplied vertices *data* values are keys in the graph's table dictionary, I add the other vertice's *data* value as a key to the dictionary inside that key's value.
    - I also add the supplied weight to the value of that inner dictionary key for both supplied vertices.
    - If the one of the supplied vertices is not found in the graph, I return a KeyError letting the caller know which vertex was not found.

- `get_vertices(self)`
    - I create an empty list
    - Then I append each key found in the graph's table dictionary into that list.
    - If the graph is empty, the list will be empty and the method will return *__None__*

- `get_neighbors(self, vertex)`
    - If the supplied vertex is a key in the graph's table dictionary, I return the value (dictionary) found at that key.
    - If the supplied vertex is not a key in the graph's table, I return a KeyError letting the caller know the vertex was not found.

- `size(self)`
    - I return the number of keys in the graph's table dictionary.

## Efficiency
- `add_vertex(self, data)`

    BigO of time is O(1)

    BigO of space is O(n)

- `add_edge(self, vert_one, vert_two, weight=0)`

    BigO of time is O(n)
    
    BigO of space is O(n)

- `get_vertices(self)`

    BigO of time is O(n)
    
    BigO of space is O(n)

- `get_neighbors(self, vertex)`

    BigO of time is O(1)
    
    BigO of space is O(1)
    
- `size(self)`

    BigO of time is O(1)
    
    BigO of space is O(1)