#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
from collections import defaultdict

Point = namedtuple("Point", ['x', 'y', 'ptno'])

""" Function to return euclidean distance between two points """
def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


""" Function to create output in the desired format, i.e.,
     a list on vertices in the order they are visited from
     a list of edges """
def createsequence(edgelist, n):

    # Using two dictionaries to store where each vertex is connected
    dict1 = {}
    dict2 = {}


    for i in edgelist:
        # since a vertex is connected to two other vertices,
        # each dictionary will store one vertex 
        if i[0] in dict1:
            dict2[i[0]] = i[1]
        else:
            dict1[i[0]] = i[1]

        if i[1] in dict1:
            dict2[i[1]] = i[0]
        else:
            dict1[i[1]] = i[0]

    res = [0]

    # create the sequence by checking where the vertex is connected 
    while len(res) < n:

        if dict1[res[len(res)-1]] in res:
            res.append(dict2[res[len(res)-1]])

        else:
            res.append(dict1[res[len(res)-1]])

    return res

""" To check if adding a new edge makes the graph cyclic """
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

""" Main greedy solution -
    Sort the edges in the increasing order of their length
    Keep selecting the next shortest edge if it does not form a loop in the graph 
    until number of edges equals number of vertices """
def sol(pts, n):

    # Creating list that hold distance between every point and every other point
    distance_list = []
    for i in range(n-1):
        for j in range(i+1,n):
            distance_list.append([length(pts[i],pts[j]),pts[i],pts[j]])
    
    # Sort the list in ascending order
    distance_list.sort()

    # Create a list that stores the degree of each vertex
    degree   =  [0] * n

    # Keep count of number of edges
    edges    =  0
    edgelist =  []

    # Initialize a graph with given number of points
    graph1   =  Graph(n)

    for i in distance_list:

        # If number of edges equals to number of points, no need to continue
        if edges == n  :
            break
        
        # If both the vertices in the edgelist currently have degree less than two,
        # and adding edge to the grapg does not result in a loop, the edge is added 
        # to the graph and degrees of the vertices and number of edges are updated
        if degree[i[1].ptno] < 2 and degree[i[2].ptno] < 2:
            if graph1.addEdge(i[1].ptno, i[2].ptno) == True:

                edgelist.append([i[1].ptno, i[2].ptno])
                degree[i[1].ptno] += 1
                degree[i[2].ptno] += 1
                edges += 1

    # Find the vertices that have degree 1, there is a missing edge between these vertices 
    # which needs to be added         
    temp = [0]*n
    for i in edgelist:
        temp[i[0]] += 1
        temp[i[1]] += 1 
     
    missingedge = []
    for i in range(n):
        if temp[i] == 1:
            missingedge.append(i)
            temp[i] += 1
    
    # Add the missing edge and return the edgelist
    edgelist.append(missingedge)
   
    return edgelist
