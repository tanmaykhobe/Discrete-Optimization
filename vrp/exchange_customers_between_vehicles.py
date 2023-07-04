import math
import random

def length(customer1, customer2):
    return math.sqrt((customer1.x - customer2.x)**2 + (customer1.y - customer2.y)**2)


""" function to return the total cost of the tour """
def totalcost(vehicle_tours, customers, vehicle_count):
    
    depot = customers[0]
    obj = 0

    for v in range(vehicle_count):
        vehicle_tour = vehicle_tours[v]
        
        if len(vehicle_tour) > 0:
            obj += length(depot,customers[vehicle_tour[0]])
            for i in range(0, len(vehicle_tour)-1):
                obj += length(customers[vehicle_tour[i]],customers[vehicle_tour[i+1]])
            obj += length(customers[vehicle_tour[-1]],depot)

    return obj


""" function to return the cummulative demands of customers on a particular route v """
def pathdemand(customers, v):

    curr_demand = 0
    for i in v:
        curr_demand += customers[i].demand

    return curr_demand


""" two opt function that optimizes the provided vehicle tours 
    by swapping two customers generated randomly in a particular tour
    and accepts the solution if the tour cost of generated tour is 
    less than original cost """     
def opt2(vehicletours, customers):

    depot = customers[0]
    
    for vehicle_tour in vehicletours:
        tour_length = len(vehicle_tour)

        if tour_length>=2:

            # find the cost of current tour
            currCost = 0
            currCost += length(depot, customers[vehicle_tour[0]])
            for i in range(tour_length-1):
                currCost += length(customers[vehicle_tour[i]],customers[vehicle_tour[i+1]])
            currCost += length(customers[vehicle_tour[-1]], depot)

            # randomly generate two customers for specified number of iterations
            for _ in range(1000):
                newCost = 0
                n1 = random.randint(0, tour_length-1)
                n2 = random.randint(0, tour_length-1)
                vehicle_tour[n1], vehicle_tour[n2] = vehicle_tour[n2], vehicle_tour[n1]

                # calculate new cost of tour after swapping
                newCost += length(depot, customers[vehicle_tour[0]])
                for i in range(tour_length-1):
                    newCost += length(customers[vehicle_tour[i]],customers[vehicle_tour[i+1]])
                newCost += length(customers[vehicle_tour[-1]], depot)
                
                # if the new cost is greater, swap the customers back, otherwise no change
                if newCost >= currCost:
                    vehicle_tour[n1], vehicle_tour[n2] = vehicle_tour[n2], vehicle_tour[n1]
   
    return vehicletours

def myfun(customers, customer_count, vehicle_count, vehicle_capacity):

    vehicle_tours = []

    # build a trivial solution
    # assign customers to vehicles starting by the largest customer demands    
    remaining_customers = set(customers)
    remaining_customers.remove(customers[0])
    
    for v in range(0, vehicle_count):
        
        vehicle_tours.append([])
        capacity_remaining = vehicle_capacity
        while sum([capacity_remaining >= customer.demand for customer in remaining_customers]) > 0:

            used = set()
            order = sorted(remaining_customers, key=lambda customer: -customer.demand*customer_count + customer.index)

            for customer in order:
                if capacity_remaining >= customer.demand:
                    capacity_remaining -= customer.demand
                    vehicle_tours[v].append(customer.index)
                    used.add(customer)
            remaining_customers -= used

    # checks that the number of customers served is correct
    assert sum([len(v) for v in vehicle_tours]) == len(customers) - 1



    for _ in range(100):

        # optimize the current vehicle tours
        vehicle_tours = opt2(vehicle_tours, customers)

        v1 = random.randint(0, vehicle_count-1)

        if len(vehicle_tours[v1]) >= 1:

            c1 = random.randint(0, len(vehicle_tours[v1])-1)
            curr_cost = totalcost(vehicle_tours, customers, vehicle_count)

            for __ in range(100-_):

                v2 = random.randint(0, vehicle_count-1)

                if len(vehicle_tours[v2]) >= 1:

                    c2 = random.randint(0, len(vehicle_tours[v2])-1)

                    if v2 != v1:

                        if pathdemand(customers, vehicle_tours[v1]) - customers[vehicle_tours[v1][c1]].demand + customers[vehicle_tours[v2][c2]].demand <= vehicle_capacity:

                            if pathdemand(customers, vehicle_tours[v2]) - customers[vehicle_tours[v2][c2]].demand + customers[vehicle_tours[v1][c1]].demand <= vehicle_capacity:

                                """ generate two customers at random from two vehicles and swap them if 
                                    it does not violate the capacity constraints of the vehicle"""
                                """ store original tour in another list """
                                tour1 = vehicle_tours[v1]
                                tour2 = vehicle_tours[v2]
                                vehicle_tours[v1][c1], vehicle_tours[v2][c2] = vehicle_tours[v2][c2], vehicle_tours[v1][c1]

                                vehicle_tours = opt2(vehicle_tours, customers)
                                new_cost = totalcost(vehicle_tours, customers, vehicle_count)

                                """ if new cost is less, accept the swap, otherwise restore the tours """
                                if new_cost < curr_cost and pathdemand(customers,vehicle_tours[v1]) <= vehicle_capacity and pathdemand(customers,vehicle_tours[v1]) <= vehicle_capacity:
                                    curr_cost = new_cost
                                    break
                                
                                else:
                                    vehicle_tours[v1] = tour1
                                    vehicle_tours[v2] = tour2

    return vehicle_tours


    
