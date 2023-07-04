import random
import math

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


""" Working of the 2-opt optimization algorithm - 
    Given a fesible solution, """
def optimize(points, n, edges):

    # Using already available feasible solution     
    edgelist = edges

    # Select two edges at random and try to change configuration if of less cost
    m = 100000
    for i in range(m):
        e1 = random.randrange(0, n)
        e2 = random.randrange(0, n)
        p1, p2, p3, p4 = edgelist[e1][0], edgelist[e1][1], edgelist[e2][0], edgelist[e2][1]
        if p1 != p3 and p1 != p4 and p2 != p3 and p2 != p4:

            # Compare the current cost of the solution with costs of other two configurations
            currcost = length(points[p1],points[p2]) + length(points[p3],points[p4])
            newcost1  = length(points[p1],points[p3]) + length(points[p2],points[p4])
            newcost2  = length(points[p1],points[p4]) + length(points[p2],points[p3])

            # For both new configurations, one of the configuration will form multiple loops in the tour
            if newcost1 < currcost and newcost2 < currcost:
                flag1 = False
                flag2 = False

                # Select the tour that does not form multiple loops and has lowest tour cost
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
                    

            elif newcost2 < currcost:
                if multipleloops2(edgelist, e1, e2, p1, p4, p2, p3, n) == 0:
                    edgelist[e1] = [p1, p4]
                    edgelist[e2] = [p2, p3]
                    
            
    return createsequence(edgelist, n)