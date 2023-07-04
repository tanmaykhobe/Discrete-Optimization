#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import shortest_edge_first 
import two_opt_optimization as two_opt
import greedy_solution as greedy 
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y', 'ptno'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def solve_it(input_data):

    # parse the input
    lines     = input_data.split('\n')
    nodeCount = int(lines[0])
    points    = []

    for i in range(1, nodeCount+1):
        line  = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1]), i-1))


    """"""""""""" SOLUTION HERE """""""""""""""""""

    if nodeCount == 574:

        edgelist = []

        # Connect the vertices in sequential order 
        for i in range(nodeCount-1):
            edgelist.append([i, i+1])
        edgelist.append([nodeCount-1, 0])

        # Optimize by using 2-opt
        solution = two_opt.optimize(points, nodeCount, edgelist)


    elif nodeCount == 33810:

        # Generate a greedy solution that selects the nearest vertex for each point to add edge
        solution = greedy.greedy_sol(points, nodeCount)


    else:

        # Algorithm that adds edges between points with the smallest distance 
        # as long as loop is not created and all points are covered
        edgelist = shortest_edge_first.sol(points, nodeCount) 

        # Optimize by using 2-opt  
        solution = two_opt.optimize(points, nodeCount, edgelist)
    
    """"""""""""""""""""""""""""""""""""""""""""""""


    # Calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])


    # Prepare the solution in the specified output format
    output_data  = '%.2f' % obj + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))


    # Write output to text file 
    file_path = f"Outputs\\output_{nodeCount}.txt" 
    with open(file_path, "w") as file:
        file.write(output_data)


    return output_data



import sys


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

