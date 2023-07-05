# Knapsack Problem Solver

This directory contains modules for solving the Knapsack problem using different approaches.

## Modules Description

1. `submit.py`:
   - This is the main file that is executed using the command `python ./submit.py` in the terminal.
   - It connects to Coursera and retrieves the problem data from the `data` directory.

2. `solver.py`:
   - This file is called when `submit.py` is run.
   - It contains the `solver` function that returns the output data required to pass the assignment.
   - The `solver` function calls two modules: `knapsack_greedy` and `knapsack_dp` to solve the Knapsack problem.

3. `knapsack_greedy.py`:
   - This module implements a greedy algorithm to solve the Knapsack problem.
   - The algorithm works as follows:
     - It sorts the items based on their value-to-weight ratio in decreasing order.
     - Then, it iterates through the sorted items and selects each item if adding it to the knapsack does not exceed the maximum weight.
     - The function keeps track of the total weight and value of the selected items and creates a binary list `objects_taken` indicating whether each item is taken (1) or not taken (0).
     - If the current weight exceeds the maximum weight, the function breaks out of the loop.
   - Finally, the function returns a list with the total value (`final_value`) and the binary list `objects_taken` representing the selected items.

4. `knapsack_dp.py`:
   - This module uses a dynamic programming approach to solve the Knapsack problem.
   - The algorithm works as follows:
     - It creates a 2D table `K` with dimensions `(item_count + 1) x (max_weight + 1)`, where `K[i][j]` represents the maximum value achievable with a weight limit of `j` considering the first `i` items.
     - The function iterates through each item and weight combination, starting from the base case of no items and zero weight (i.e., `K[0][w] = 0` for all `w` and `K[i][0] = 0` for all `i`).
     - For each item and weight combination, the function checks whether including the current item would be beneficial or not. It compares the value of including the item (value of the current item plus the value achieved with the remaining weight) with the value achieved without including the item (value achieved with the previous items).
     - The function fills the table `K` based on these comparisons.
     - After filling the table, it retrieves the maximum value achieved (`res`) from `K[item_count][max_weight]`.
     - Then, it backtracks through the table to determine which items were included in the optimal solution. It checks whether the value at `K[i][w]` is the same as the value without including the current item (`K[i - 1][w]`). If not, it includes the item in the solution and subtracts its value and weight from the remaining values.
   - Finally, the function returns a list with the total value (`res`) and a binary list `include` representing the inclusion (1) or exclusion (0) of each item in the optimal solution.

The provided modules offer different approaches to solve the Knapsack problem, allowing for flexibility in choosing the most suitable algorithm based on the problem requirements and constraints.
