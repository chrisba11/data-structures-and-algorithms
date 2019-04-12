# Pre-Order Depth First Graph Traversal
Function that takes in a graph and a starting node and returns a list of all of the nodes traversed in a pre-order depth-first manner.

## Challenge
- Create a function that accepts an adjacency list as a graph, and conducts a depth first traversal. Without utilizing any of the built-in methods available to your language, return a collection of nodes in their pre-order depth-first traversal order.

## Approach
- I created a stack and an output list
- If the provided start_vertex is found in the graph...
    - I push the start_vertex into the stack
    - I append it to the output list
    - I set it to show as visited
- I then run a recursive function that will check the stack to see if it has any items.
- If so, it will set current to the item at the top of the stack.
- It will then run through all of the neighbors of the current and push any unvisited items into the stack, append them to the output list, and set them as visited.
- The function will then call itself.
- If the stack is empty, it will run through every vertex in the graph and reset them to unvisited.
- Finally, it will output the output list.

## Efficiency
- The BigO for time is O(n) because it traverses every node in the graph.
- The BigO for space is O(n) because it creates a stack that will equal the size of the number of nodes in the graph and outputs an array whose length will equal the number of nodes in the graph.

## Solution
![depth_first_graph image](../assets/depth_first_graph.jpg)



