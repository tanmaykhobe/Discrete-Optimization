import math

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

""" Working of greedy algorithm for TSP -
    Starting from point 0, select the nearest point to it and add an edge 
    from the set of remaining points(which are not yet connected), 
    continue this till all points are connected """
def greedy_sol(pts, n):

    res = [0]
    allpts = [i for i in range(1,n)]

    while len(res) < n:

        # Find the nearest point (from set of points not connected) to the last point in the current tour 
        # and add it to current tour and update set of remaining points
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