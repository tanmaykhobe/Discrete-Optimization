#!/usr/bin/python
# -*- coding: utf-8 -


import knapsack_greedy as greedy
import knapsack_dp as dp
from collections import namedtuple


def solve_it(input_data):


    # parse the input
    lines      = input_data.split('\n')
    firstLine  = lines[0].split()
    item_count = int(firstLine[0])
    capacity   = int(firstLine[1])
    weights  = []
    values   = []


    for i in range(1, item_count+1):
        line  = lines[i]
        parts = line.split()
        values.append (int(parts[0]))
        weights.append(int(parts[1]))


    """ For very high number of items, the greedy approach works better 
    as it sorts items by value by weight ratio """
    if item_count == 400 or item_count == 10000:
        res = greedy.greedy_function(capacity, weights, values, item_count)
    
    # For other problems the dynamic programming approach is better
    else:
        res = dp.dp_function(capacity, weights, values, item_count)


    final_value   = res[0]
    objects_taken = res[1]
    

    # prepare the solution in the specified output format
    output_data = str(final_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, objects_taken))
    return output_data




if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

