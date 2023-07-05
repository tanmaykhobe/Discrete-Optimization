This code implements a color assignment algorithm for a graph using a greedy approach. The goal is to assign colors to the nodes of the graph in such a way that no two adjacent nodes have the same color. The algorithm uses a priority queue to prioritize nodes based on their degrees (number of edges connected to a node) in reverse order.

Here is a summary of how the code works:

1. Initialize data structures:
   - `pq`: A priority queue to store nodes based on degrees.
   - `degrees`: A list to store the degrees of each node.
   - `adjacency_list`: A defaultdict of lists to store the neighbors of each node.
   - `colors`: A list to store the assigned colors for each node.

2. Populate `degrees` and `adjacency_list` based on the given `edge_list`.

3. Populate the priority queue `pq` with nodes sorted by degrees in reverse order.

4. Iteratively assign colors to nodes:
   - Get the node with the highest degree from `pq`.
   - Check the colors of adjacent nodes and store them in the `adjacent_colors` set.
   - Assign the lowest available color to the current node by finding the first non-conflicting color.
   - Update the `colors` list with the assigned color for the current node.

5. Write the color assignments to the "Output.txt" file:
   - Open the output file in write mode.
   - Write the color assignment chart, showing the assigned color for each node.
   - Calculate the maximum color used.
   - Close the output file.

6. Return the `colors` list and the total number of colors used.

The algorithm ensures that no two adjacent nodes have the same color by checking the colors of the neighbors of each node. It greedily assigns colors to nodes based on the availability of colors and the colors of neighboring nodes.

Note: The code assumes that the input graph is connected, i.e., there is a path between every pair of nodes. If the graph is not connected, this algorithm will assign colors independently to each connected component of the graph.
