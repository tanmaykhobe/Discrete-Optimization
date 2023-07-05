# Facility Location Problem Solver

This code utilizes the OR-Tools library to solve a facility location problem using the SCIP solver. The objective of the problem is to determine the optimal configuration of facilities and their corresponding customer assignments to minimize the total cost, which includes setup costs and distances between customers and facilities.

## Summary

The code follows the steps outlined below:

1. Define the `length` function, which calculates the Euclidean distance between two points using their coordinates.

2. Define the `solver_using_scip` function, which takes two input lists: `facilities` and `customers`.

3. Set up the SCIP solver and configure the time limit for solving the problem based on the number of facilities.

4. Create decision variables using `BoolVar` to represent the facility status (open/closed) and facility-customer assignments.

5. Define the constraints:
   - Each customer must be served by exactly one facility.
   - The sum of demands of customers served by a facility must be less than or equal to the facility's capacity.
   - A facility can only serve a customer if it is open.

6. Define the objective function:
   - Minimize the sum of setup costs for open facilities.
   - Minimize the sum of distances between customers and their assigned facilities.

7. Call the `solver.Solve()` method to solve the problem.

8. Retrieve the solution:
   - Iterate over the decision variables to determine the facility index serving each customer.
   - Store the facility indices in the `res` list.

9. Return the `res` list, which represents the facility indices serving each customer.

This code leverages the SCIP solver from the OR-Tools library to find the optimal solution for the facility location problem. By formulating the problem as a mixed-integer linear programming (MILP) model and applying appropriate constraints and an objective function, it determines the optimal assignment of facilities and customers to minimize the total cost.
