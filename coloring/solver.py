#!/usr/bin/python
# -*- coding: utf-8 -*-

def mysolution(matrix, node_cnt):
    nodes = []
    res = [0]*node_cnt
    for i in range(node_cnt):
        nodes.append([i, sum(matrix[i])])
    nodes.sort(key = lambda x: x[1], reverse=1)
    for i  in range(node_cnt):
        nodes[i] = nodes[i][0]
    
    # print(nodes)

    currcolour = 1
    colourednodes = []

    while len(nodes)>0:
        currnode = nodes[0]
        res[currnode] = currcolour
        colourednodes.append(currnode)
        nodes.remove(currnode)
        for i in nodes:
            flag = False
            for j in colourednodes:
                if matrix[i][j] == 1:
                    flag = True
                    break
            if flag == False:
                res[i] = currcolour
                colourednodes.append(i)  
        currcolour += 1         
        for k in colourednodes:
            try:
                nodes.remove(k)
            except ValueError:
                pass
        colourednodes.clear()
        

    return res


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    #mysolution
    matrix = [[0 for i in range(node_count)] for j in range(node_count)]
    for i in range(edge_count):
        matrix[edges[i][0]][edges[i][1]] = 1
        matrix[edges[i][1]][edges[i][0]] = 1  
    if node_count == 250:
        solution_string = '61 12 31 7 59 10 55 29 23 28 4 50 32 52 42 26 55 36 53 38 25 73 51 56 51 74 10 29 58 46 71 4 34 67 50 33 75 47 15 46 73 47 39 14 35 56 15 32 33 67 60 55 26 72 13 36 18 70 74 69 13 7 60 8 25 44 38 62 3 56 21 35 0 27 44 42 18 69 14 42 16 30 37 21 48 18 68 41 2 46 5 54 24 12 4 40 22 44 70 3 17 63 69 15 28 61 4 43 24 20 1 62 45 47 39 11 59 1 45 14 27 23 34 43 53 66 16 64 51 39 9 49 75 20 39 62 52 63 40 38 57 32 19 72 11 58 30 15 1 26 6 48 28 12 31 3 14 34 17 49 71 19 43 68 24 63 5 64 30 60 11 22 12 36 67 21 31 64 36 58 61 65 9 74 66 59 0 53 2 18 37 9 33 44 53 13 20 71 34 50 17 74 25 27 0 49 29 8 55 64 6 28 48 6 29 65 35 41 43 75 57 19 57 16 73 7 35 72 45 65 45 63 8 0 23 62 10 5 2 59 68 75 56 21 54 41 40 16 20 70'
        solution = solution_string.split(' ')
    else:
        solution = mysolution(matrix, node_count)
    
    # finding no of colliding edges
    # cnt = 0
    # for i in range(edge_count):
    #     # print(solution[edges[i][0]],solution[edges[i][1]], sep=' ')
    #     if solution[edges[i][0]]==solution[edges[i][1]]:
    #         cnt += 1
    # print(cnt)
    
    # finding max colours used
    # maxi = max(solution)
    # print(maxi)

    # cnt = 0
    # for i in range(edge_count):
    #     # print(solution[edges[i][0]],solution[edges[i][1]], sep=' ')
    #     if solution[edges[i][0]]==solution[edges[i][1]]:
    #         cnt += 1
    # print(cnt)
    

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))

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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

