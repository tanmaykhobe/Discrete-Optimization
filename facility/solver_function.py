# solution using scip solver

from ortools.linear_solver import pywraplp
import math


def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


def myfun(facilities, customers):
    no_f = len(facilities)
    no_c = len(customers)


    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    time_limit = 1800
    if no_f >= 500:
        time_limit *= 3
    solver.SetTimeLimit(int(time_limit * 1000))

    # DECISION VARIABLES
    open = {}
    x = {}
    for i in range(no_f):
        open[i] = solver.BoolVar(f'open{i}')
        for j in range(no_c):
            x[i,j] = solver.BoolVar(f'x{i}{j}')


    # print('Number of variables =', solver.NumVariables())
    


    #CONSTRAINTS
    for i in range(no_c):
        tempsum = 0
        tempsum += solver.Sum(x[j,i] for j in range(no_f))
        solver.Add(tempsum == 1)

    for i in range(no_f):
        sumOfDemands = 0
        sumOfDemands += solver.Sum(customers[j].demand * x[i,j] for j in range(no_c))
        solver.Add(sumOfDemands <= facilities[i].capacity)
    
    for i in range(no_f):
        sumrow = 0
        for j in range(no_c):
            sumrow += x[i,j]
        solver.Add(sumrow <= no_c * open[i])
            
        
    # print('Number of constraints =', solver.NumConstraints())
            
    # OBJECTIVE
    sumSetup = 0
    for i in range(no_f):
        sumSetup += open[i] * facilities[i].setup_cost 
    
    sumDist = 0
    for i in range(no_f):
        for j in range(no_c):
                sumDist += length(facilities[i].location, customers[j].location) * x[i,j]

    solver.Minimize(sumDist + sumSetup)

    # print(f'Solving with {solver.SolverVersion()}')
    solver.Solve()

    # if status == pywraplp.Solver.OPTIMAL:
    #     print('Solution:')
    #     print('Objective value =', solver.Objective().Value())
    #     # # Print decision variable values
    #     # for i in range(no_f):
    #     #     for j in range(no_c):
    #     #         print(f'x[{i},{j}] =', x[i, j].solution_value())

    # else:
    #     print('The problem does not have an optimal solution.')
    
    res = [-1]*no_c
    for i in range(no_f):
        for j in range(no_c): 
            if x[i,j].solution_value() == 1 :
                res[j] = i
    
    return res