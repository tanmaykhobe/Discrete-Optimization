#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def greedy(W, wt, val, n):
    valperkg = []
    for i in range(n):
        valperkg.append([val[i]/wt[i],i])
    valperkg.sort(reverse=True)    
    # print(valperkg) 
    taken = [0]*n
    currwt = 0
    res = 0
    for i in range(n):
        if currwt + wt[valperkg[i][1]] <= W:
            currwt += wt[valperkg[i][1]]
            res += val[valperkg[i][1]]
            taken[valperkg[i][1]] = 1
        if currwt > W:
            break
    # print(taken)
    ans = []
    ans.append(res)
    ans.append(taken)
    return ans

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for y in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                              + K[i-1][w-wt[i-1]],
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    res = K[n][W]
    ans = []
    ans.append(int(res))
    incldd = []
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            incldd.append(int(0))
            # break
        elif res == K[i - 1][w]:
            incldd.append(int(0))
        else:
            incldd.append(int(1))
            res = res - val[i - 1]
            w = w - wt[i - 1]
    incldd.reverse()
    ans.append(incldd)
    # print(ans)
    # print(*K,  sep = "\n")
    return ans

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []
    wtss = []
    valss = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        # items.append(Item(i-1, int(parts[0]), int(parts[1])))
        valss.append(int(parts[0]))
        wtss.append(int(parts[1]))


    # a trivial algorithm for filling the knapsack
    # # it takes items in-order until the knapsack is full
    if item_count == 400 or item_count == 10000:
        ans2 = greedy(capacity, wtss, valss, item_count)
    else:
        ans2 = knapSack(capacity, wtss, valss, item_count)
    value = ans2[0]
    # weight = ans2[1]
    taken = ans2[1]

    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight
    

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
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

