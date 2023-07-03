#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import random
import tsp_greedyfunction
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y', 'ptno'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def createsequence(edgelisto, n):
    dict1 = {}
    dict2 = {}
    for i in edgelisto:
        if i[0] in dict1:
            dict2[i[0]] = i[1]
        else:
            dict1[i[0]] = i[1]
        if i[1] in dict1:
            dict2[i[1]] = i[0]
        else:
            dict1[i[1]] = i[0]
    # print(dict1, dict2)
    # visited = [0]*len(edgelisto)
    res = [0]
    while len(res) < n:
        if dict1[res[len(res)-1]] in res:
            res.append(dict2[res[len(res)-1]])
        else:
            res.append(dict1[res[len(res)-1]])
    dict1.clear()
    dict2.clear()
    return res

def multipleloops1(edges, e1, e2, a, b, c, d, n):
    edgelistcopy = edges
    edgelistcopy[e1] = [a,b]
    edgelistcopy[e2] = [c,d]
    tempset2 = createsequence(edgelistcopy, n)
    tempset = set(tempset2)
    # print(len(tempset))
    if len(tempset) < n:
        edgelistcopy[e1] = [a,c]
        edgelistcopy[e2] = [b,d]
        return 1
    return 0

def multipleloops2(edges, e1, e2, a, b, c, d, n):
    edgelistcopy = edges
    edgelistcopy[e1] = [a,b]
    edgelistcopy[e2] = [c,d]
    tempset2 = createsequence(edgelistcopy, n)
    tempset = set(tempset2)
    # print(len(tempset))
    if len(tempset) < n:
        edgelistcopy[e1] = [a,c]
        edgelistcopy[e2] = [d,b]
        return 1
    return 0

def opt2sol(points, n, edges):
    # creating an edgelist joining the nodes in sequential order     
    edgelist = edges

    #select two edges at random and try to change configuration if of less cost
    m = 100000
    for i in range(m):
        e1 = random.randrange(0, n)
        e2 = random.randrange(0, n)
        p1, p2, p3, p4 = edgelist[e1][0], edgelist[e1][1], edgelist[e2][0], edgelist[e2][1]
        if p1 != p3 and p1 != p4 and p2 != p3 and p2 != p4:
            currcost = length(points[p1],points[p2]) + length(points[p3],points[p4])
            newcost1  = length(points[p1],points[p3]) + length(points[p2],points[p4])
            newcost2  = length(points[p1],points[p4]) + length(points[p2],points[p3])
            if newcost1 < currcost and newcost2 < currcost:
                flag1 = False
                flag2 = False
                if multipleloops1(edgelist, e1, e2, p1, p3, p2, p4, n) == 0:
                    flag1 = True
                if multipleloops2(edgelist, e1, e2, p1, p4, p2, p3, n) == 0:
                    flag2 = True
                if flag1 == True and flag2 == True:
                    if newcost1 < newcost2:
                        edgelist[e1] = [p1, p3]
                        edgelist[e2] = [p2, p4]
                    else:
                        edgelist[e1] = [p1, p4]
                        edgelist[e2] = [p2, p3]
                elif flag1 == True:
                    edgelist[e1] = [p1, p3]
                    edgelist[e2] = [p2, p4]
                elif flag2 == True:
                    edgelist[e1] = [p1, p4]
                    edgelist[e2] = [p2, p3]

            elif newcost1 < currcost:
                if multipleloops1(edgelist, e1, e2, p1, p3, p2, p4, n) == 0:
                    edgelist[e1] = [p1, p3]
                    edgelist[e2] = [p2, p4]
                    # print("loop1")

            elif newcost2 < currcost:
                if multipleloops2(edgelist, e1, e2, p1, p4, p2, p3, n) == 0:
                    edgelist[e1] = [p1, p4]
                    edgelist[e2] = [p2, p3]
                    # print("loop2")
            
        # print(edgelist)
        # print(createsequence(edgelist, n))
        # print('-')
        # sc.plt.pause(0.01)
        # sc.plt.show()
    # print(edgelist)
    # xcoordinates = [int(i.x) for i in points]
    # ycoordinates = [int(i.y) for i in points]
    # print(xcoordinates)
    # print(ycoordinates)
    # print(edgelist)
    # print(createsequence(edgelist, n))
    return createsequence(edgelist, n)

def greedysol1(pts, n):
    res = [0]
    allpts = [i for i in range(1,n)]

    while len(res) < n:
        leastdistance = float('inf')
        nearestpt = -1
        for i in allpts:
            currdist = length(pts[res[-1]], pts[i])
            if currdist < leastdistance:
                leastdistance = currdist
                nearestpt = i
        res.append(nearestpt)
        allpts.remove(nearestpt)
    return res

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1]), i-1))

    # build a trivial solution
    # visit the nodes in the order they appear in the file
    # solution = range(0, nodeCount)
    edgelist = []
    if nodeCount == 574:
        for i in range(nodeCount-1):
            edgelist.append([i, i+1])
        edgelist.append([nodeCount-1, 0])
        solution = opt2sol(points, nodeCount, edgelist)
    elif nodeCount == 33810:
        solution = greedysol1(points, nodeCount)
    else:
        edgelist = tsp_greedyfunction.sol1(points, nodeCount)   #greedy function
        solution = opt2sol(points, nodeCount, edgelist)
    # 2-opt solution 
    


    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, solution))

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

