The travelling salesman problem has been implemented using various approaches.\
\
One of the approaches is generating a greedy solution which works as follows -\
  Starting from a random point, say point 0, find its nearest point and add an edge. Keep adding edges from the last point in tour but finding the nerest point such that loop is not created. When all possible edges are exhausted, find the points having degree 1 in the tour and add the missing edge between these points.\
  Another approach is similar to Kruskal's Minimum Spanning tree algorithm. From the set of all possible edges, keep selecting the shortest edge and add it to a graph while checking for cycle in the graph. If a cycle is created by adding some edge, the edge is not selected. Continue until all the edges are not exhausted or a limiting condition is reached (number of edges equals number of vertices).\
  One of the techniques used for optimizing a feasible solution is the 2-opt technique which removes two edges and finds a configuration with two new edges that has minimum cost over a number of iterations.
  
 
The information regarding various python files is as follows -
1. solver.py:\
  The module imports several helper scripts and libraries, including math, shortest_edge_first, two_opt_optimization, and greedy_solution.\
  It defines a named tuple Point to represent a point in the TSP problem, consisting of its x and y coordinates and a point number.\
  The length function calculates the Euclidean distance between two points.\
  The solve_it function takes an input data string as a parameter and solves the TSP based on the input.\
  Inside the solve_it function, the input data is parsed to extract the node count and the coordinates of the points.\
  The solution logic is implemented in the section marked as "SOLUTION HERE". There are specific solution approaches for different node counts (574 and 33810), and a default approach for other cases.\
  The solution is obtained by applying the appropriate algorithm(s) to find an initial solution and then optimizing it using the 2-opt technique.\
  The length of the tour is calculated by summing the distances between consecutive points in the solution.\
  The output data is prepared in the specified format, including the tour length and the order of visited points.\
  The output data is written to a text file named output_<nodeCount>.txt in the "Outputs" directory.\
  Finally, the output data is returned by the solve_it function.

2. shortest_edge_first:\
   The code begins by importing necessary modules and defining a named tuple called Point to represent a point with its coordinates and point number.\
  The length function calculates the Euclidean distance between two points using their coordinates.\
  The createsequence function takes an edge list and the number of vertices as input and generates a sequence of vertices in the order they are visited. It uses dictionaries to store the connections between vertices and constructs the sequence based on these connections.\
  The Graph class represents a graph using an adjacency list and provides methods for adding edges and finding the root of a disjoint set using the union-find algorithm.\
  The sol function is the main greedy solution for the TSP. It takes a list of points and the number of vertices as input. It calculates the distances between points and sorts them in ascending order. Then it iterates through the sorted distances, adding edges to the graph if they do not create a loop and if the degree of the vertices is less than two. The process continues until the number of edges equals the number of vertices. Finally, it identifies the vertices with degree 1 and adds a missing edge between them.\
  Overall, the code aims to find a Hamiltonian cycle (a cycle that visits each vertex exactly once) with a minimal total distance using a greedy approach.

3. greedy_solution:\
  The greedy_sol function implements a greedy algorithm to solve the traveling salesman problem (TSP). It takes a list of points (pts) and the number of vertices (n) as input.\
  The function initializes an empty list called res to store the resulting tour. It also creates a list called allpts containing all the points except the starting point (point 0).\
  The algorithm iteratively selects the nearest point (from the set of points not yet connected) to the last point in the current tour. It calculates the distance between the last point in the tour and each remaining point using the length function. The point with the shortest distance is chosen as the nearest point and added to the tour.\
  The process continues until all points have been connected, i.e., until the length of the resulting tour (res) is equal to the total number of vertices (n).\
  Finally, the function returns the resulting tour (res), which represents a Hamiltonian cycle visiting each vertex exactly once.\
The code implements a simple and intuitive greedy algorithm for the TSP, but it may not always find the optimal solution.

4. two_opt_optimization:\
  The createsequence function takes an edgelist and the number of vertices as input. It creates two dictionaries (dict1 and dict2) to store the connections between vertices. The function iterates through the edgelist and populates the dictionaries accordingly. Then, it creates a sequence of vertices by traversing the connections in the dictionaries. The resulting sequence is returned.\
  The multipleloops1 and multipleloops2 functions are helper functions used in the optimization algorithm. They take an edgelist, two edges to modify, and four vertices as input. These functions attempt to change the configuration of the two edges and check if the resulting tour contains multiple loops. If multiple loops are detected, the changes are reversed, and the function returns 1. Otherwise, it returns 0.\
  The optimize function implements the 2-opt optimization algorithm. It takes a list of points (points), the number of vertices (n), and an initial edgelist (edges) as input.\
  The function iterates a fixed number of times (m) and randomly selects two edges to modify. It compares the current cost of the solution with the costs of two alternative configurations formed by changing the edges.\
  If both alternative configurations have lower costs and do not form multiple loops, the function selects the one with the lowest cost and updates the edgelist accordingly.\
  If only one alternative configuration is valid (does not form multiple loops), the function updates the edgelist with that configuration.\
  After the iteration is complete, the function returns the resulting sequence obtained from the updated edgelist.\
  The additional code introduces the createsequence function to create the desired output format, as well as helper functions and an optimization algorithm to improve the initial solution using the 2-opt method.
    
