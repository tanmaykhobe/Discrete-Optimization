from ortools.linear_solver import pywraplp

def myfun(noItems, noSets, sets):

    solver = pywraplp.Solver.CreateSolver('SCIP')
    timeL = 1800
    solver.SetTimeLimit(timeL * 1000)

    
    # DECISION VARIABLES
    setStatus = {}
    
    for i in range(noSets):
        setStatus[i] = solver.BoolVar(f'status{i}')

    
    # OBJECTIVE FUNCTION
    cost = 0
    
    for i in range(noSets):
        cost += sets[i].cost * setStatus[i]
        
    solver.Minimize(cost)

    
    # CONSTRAINTS
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
    

    

    
