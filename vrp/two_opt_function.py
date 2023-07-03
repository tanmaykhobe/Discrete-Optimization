import math
import random


def length(customer1, customer2):
    return math.sqrt((customer1.x - customer2.x)**2 + (customer1.y - customer2.y)**2)


def opt2(vehicletours, customers):
    """ a two opt function that optimizes the provided vehicle tours 
    by swapping two customers generated randomly in a particular tour
    and accepts the solution if the tour cost of generated tour is 
    less than original cost """ 

    # specify depot as the first customer
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
            for _ in range(10000):
                newCost = 0
                n1 = random.randint(0,tour_length-1)
                n2 = random.randint(0,tour_length-1)

                # swap the two customers
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