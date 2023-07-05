Information about various modules included in this directory -

1. submit.py :
	The main file that will run using 'python ./submit.py' in terminal and will connect to coursera, and the data for problems is taken from 'data' directory.

2. solver.py :
	The file that is called when submit.py is run. Constains the solver functon that returns the output data required for passing the assignment consisting of value of solution, status of optimality and the actual solution in the specified format. It calls upon two modules namely 'knapsack_greedy' and 'knapsack_dp' to solve the knapsack assignment.

3. kanpsack_greedy.py :
	   - The function implements a greedy algorithm to solve the knapsack problem.
	   - It sorts the items based on their value-to-weight ratio in decreasing order.
	   - Then, it iterates through the sorted items and selects each item if adding it to the knapsack does not exceed the maximum weight.
	   - The function keeps track of the total weight and value of the selected items and creates a binary list `objects_taken` indicating whether each item is taken (1) or not taken (0).
	   - If the current weight exceeds the maximum weight, the function breaks out of the loop.
	   - Finally, it returns a list with the total value (`final_value`) and the binary list `objects_taken` representing the selected items.


4. knapsack_dp.py :
	   - The function uses a dynamic programming approach to solve the knapsack problem.
	   - It creates a 2D table `K` with dimensions `(item_count + 1) x (max_weight + 1)`, where `K[i][j]` represents the maximum value achievable with a weight limit of `j` considering the first `i` items.
	   - The function iterates through each item and weight combination, starting from the base case of no items and zero weight (i.e., `K[0][w] = 0` for all `w` and `K[i][0] = 0` for all `i`).
	   - For each item and weight combination, the function checks whether including the current item would be beneficial or not. It compares the value of including the item (value of the current item plus the value 			achieved with the remaining weight) with the value achieved without including the item (value achieved with the previous items).
	   - The function fills the table `K` based on these comparisons.
	   - After filling the table, it retrieves the maximum value achieved (`res`) from `K[item_count][max_weight]`.
	   - Then, it backtracks through the table to determine which items were included in the optimal solution. It checks whether the value at `K[i][w]` is the same as the value without including the current item (`K[i - 1][w]`). If not, it includes the item in the solution and subtracts its value and weight from the remaining values.
	   - Finally, it returns a list with the total value (`res`) and a binary list `include` representing the inclusion (1) or exclusion (0) of each item in the optimal solution.

