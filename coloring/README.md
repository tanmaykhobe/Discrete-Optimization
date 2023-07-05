# Graph Coloring Assignment 

This code implements a graph color assignment algorithm using a greedy approach. The goal is to assign colors to the nodes of the graph in such a way that no two adjacent nodes have the same color. The algorithm utilizes a priority queue to prioritize nodes based on their degrees (number of edges connected to a node) in reverse order.

## Summary

The algorithm works as follows:

1. Initialize data structures:
   - `pq`: A priority queue to store nodes based on degrees.
   - `degrees`: A list to store the degrees of each node.
   - `adjacency_list`: A `defaultdict` of lists to store the neighbors of each node.
   - `colors`: A list to store the assigned colors for each node.

2. Populate `degrees` and `adjacency_list` based on the given `edge_list`.

3. Populate the priority queue `pq` with nodes sorted by degrees in reverse order.

4. Iteratively assign colors to nodes:
   - Retrieve the node with the highest degree from `pq`.
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

This algorithm provides a simple and efficient solution for graph coloring problems, allowing for the assignment of colors to graph nodes while maintaining the constraint of no adjacent nodes having the same color.
