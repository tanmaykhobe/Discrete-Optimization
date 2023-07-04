

def dp_function(max_weight, weights, values, item_count):

    """ The dynamic programming approach for solving knapsack -
        In a K[][] table let's consider all the possible weights from '1' to 'W' as the columns and the element that can be kept as rows. 
        The state K[i][j] will denote the maximum value of 'j-weight' considering all values from '1 to ith'. So if we consider 'wi' (weight in 'ith' row) we can fill it in all columns which have 'weight values > wi'. Now two possibilities can take place: 
        Fill 'wi' in the given column.
        Do not fill 'wi' in the given column.
        Now we have to take a maximum of these two possibilities, 
        Formally if we do not fill the 'ith' weight in the 'jth' column then the K[i][j] state will be the same as K[i-1][j] 
        But if we fill the weight, K[i][j] will be equal to the value of ('wi'+ value of the column weighing 'j-wi') in the previous row. 
        So we take the maximum of these two possibilities to fill the current state. """
    
    K = [[0 for i in range(max_weight+1)] for j in range(item_count+1)]
    

    # Build table K[][] in bottom up manner
    for i in range(item_count + 1):
        for w in range(max_weight + 1):

            if i == 0 or w == 0:
                K[i][w] = 0

            elif weights[i-1] <= w:
                K[i][w] = max((values[i-1] + K[i-1][w-weights[i-1]]), K[i-1][w])

            else:
                K[i][w] = K[i-1][w]


    res = K[item_count][max_weight]
    ans = []
    ans.append(int(res))

    # find items that were included in the solution
    include = []


    w = max_weight
    for i in range(item_count, 0, -1):

        if res <= 0:
            include.append(int(0))
            
        elif res == K[i - 1][w]:
            include.append(int(0))

        else:
            include.append(int(1))
            res = res - values[i - 1]
            w = w - weights[i - 1]


    include.reverse()
    ans.append(include)

    """ return list with objective value and list of items included """
    return ans