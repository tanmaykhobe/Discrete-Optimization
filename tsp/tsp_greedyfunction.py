#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
from collections import defaultdict

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

    return res

# to check if adding a new edge makes the graph cyclic
class Graph:
    def __init__(self, V):
        self.V = V  # Number of vertices in the graph
        # List of lists to store the adjacency list of each vertex
        self.adj = [[] for _ in range(V)]
        # List to store the parent of each vertex in the disjoint set
        self.parent = list(range(V))
        # List to store the rank of each vertex in the disjoint set
        self.rank = [0] * V
    def addEdge(self, u, v):
        # Find the root of the disjoint set containing vertex u
        rootU = self.find(u)
        # Find the root of the disjoint set containing vertex v
        rootV = self.find(v)
        # print(rootU, rootV)
        if rootU == rootV:  # If u and v are already in the same disjoint set, there is no need to add the edge
            return False  # Return False to indicate that the edge was not added
        # If the rank of the disjoint set containing u is less than the rank of the disjoint set containing v
        if self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV  # Make v the parent of u
        # If the rank of the disjoint set containing u is greater than the rank of the disjoint set containing v
        elif self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU  # Make u the parent of v
        else:  # If the rank of the disjoint set containing u is equal to the rank of the disjoint set containing v
            self.parent[rootV] = rootU  # Make u the parent of v
            # Increment the rank of the disjoint set containing u
            self.rank[rootU] += 1
        self.adj[u].append(v)  # Add v to the adjacency list of u
        self.adj[v].append(u)  # Add u to the adjacency list of v
        return True  # Return True to indicate that the edge was added
 
    def find(self, u):
        # If the parent of u is not u, i.e., u is not the root of its disjoint set
        if self.parent[u] != u:
            # Recursively find the root of the disjoint set containing u and update the parent of u to point directly to the root
            self.parent[u] = self.find(self.parent[u])
        # Return the root of the disjoint set containing u
        return self.parent[u]


def sol1(pts, n):
    distancelist = []
    for i in range(n-1):
        for j in range(i+1,n):
            distancelist.append([length(pts[i],pts[j]),pts[i],pts[j]])
    distancelist.sort()
    # print(distancelist)
    degree = [0]*n
    edges = 0
    edgelist = []
    graph1 = Graph(n)
    for i in distancelist:
        if edges == n  :
            break
        if degree[i[1].ptno] < 2 and degree[i[2].ptno] < 2:
            if graph1.addEdge(i[1].ptno, i[2].ptno) == True:
                edgelist.append([i[1].ptno, i[2].ptno])
                degree[i[1].ptno] += 1
                degree[i[2].ptno] += 1
                edges += 1
                # print(degree)
    # # to check if all the nodes are connected to only two vertices or not
    # print(edgelist)   
    temp = [0]*n
    for i in edgelist:
        temp[i[0]] += 1
        temp[i[1]] += 1
    # print(temp)
    missingedge = []
    for i in range(n):
        if temp[i] == 1:
            missingedge.append(i)
            temp[i] += 1
    edgelist.append(missingedge)
    # print(missingedge)
    # print(edgelist)
    # print(temp)
    # print(len(edgelist))

    # tempans = createsequence(edgelist, n)
    # return tempans
    return edgelist
