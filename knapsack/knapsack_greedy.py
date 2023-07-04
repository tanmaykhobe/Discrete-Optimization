

def greedy_function(max_weight, weights, values, item_count):
    """ the working of greedy function is as follows -
        sort the items in the decreasing order
        of their value to weight ratio (density of value)
        and then select items according to this ratio until
        the knapsack is full """


    # list to store items in order of their value to weight ratio
    value_to_weight_ratio = []


    # add items to the list along with item number
    for i in range(item_count):
        ratio = values[i] / weights[i]
        value_to_weight_ratio.append([ratio, i])

    
    # sort the items in descending order 
    value_to_weight_ratio.sort(reverse=True)


    # specify list that stores 1 if the item is taken, 0 otherwise
    objects_taken = [0] * item_count


    current_weight = 0
    final_value   = 0


    for i in range(item_count):

        """select item if adding item to current weight of knapsack 
            does not exceed maximum weight of kanpsack"""
        if (current_weight + weights[value_to_weight_ratio[i][1]]) <= max_weight:
            current_weight += weights[value_to_weight_ratio[i][1]]
            final_value    += values[value_to_weight_ratio[i][1]]
            objects_taken[value_to_weight_ratio[i][1]] = 1

        if current_weight > max_weight:
            break


    res = []
    res.append(final_value)
    res.append(objects_taken)

    """ return list with objective value and list of objects taken """
    return res