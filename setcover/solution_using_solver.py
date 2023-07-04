from ortools.linear_solver import pywraplp


""" Goal - Select sets from given list of sets such that all items are covered and cost is minimized """
def myfun(noItems, noSets, sets):

    # The Set Cover problem is solved using MIP using pywraplp library from Google OR tools using SCIP solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Set solver time limit of half an hour
    timeL = 1800
    solver.SetTimeLimit(timeL * 1000)

    
    # DECISION VARIABLES
    # The only decision variable is the binary variable status of set, i.e., if the set is included in solution or not
    setStatus = {}
    
    for i in range(noSets):
        setStatus[i] = solver.BoolVar(f'status{i}')

    
    # OBJECTIVE FUNCTION
    # Including a set in the solution has a respective cost, and the gold is to minimize this cost
    cost = 0
    
    for i in range(noSets):
        cost += sets[i].cost * setStatus[i]
        
    solver.Minimize(cost)

    
    # CONSTRAINTS
    # The only constraint is that all the items should be covvered by the sets selected in the solution
    for j in range(noItems):
        itemSum = 0
        for i in range(noSets):
            for k in sets[i].items:
                if k == j:
                    itemSum += setStatus[i]
        solver.Add(itemSum >= 1)

    
    # SOLVE MODEL
    solver.Solve()

    res = []
    for i in range(noSets):
        res.append(int(setStatus[i].solution_value()))

    return res
    

    

    
