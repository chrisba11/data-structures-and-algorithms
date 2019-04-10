# Breadth First Graph Traversal
Function that takes in a graph and a starting node and returns a list of all of the nodes traversed in a breadth first order.

## Challenge
- Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Approach
- I instantiated a queue and and output list
- I checked to see if the provided start_vertex was in the graph.
    - If yes, I enqueue that vertex and set its visited property to True
- I then call the _traverse function while there are items in the queue.
    - Inside the _traverse function, I set curr to the dequeued value.
    - If curr has neighbors, I take any that have not been visited and enqueue them and change their visited property to True.
    - I then append curr to the output list.
- Lastly, I reset all of the vertices' visited property to False and return the output list.

## Efficiency
- The BigO of time is O(n^2) because worst case would be an edge connecting every vertex in the graph to every other vertex in the graph.
- The BigO of space is O(n) because the output list would only be as large as the number of vertices in the graph.

## Solution
![breadth_first_graph image](../assets/breadth_first_graph.jpg)



