Information about various modules included in this directory -

1. submit.py :
	The main file that will run using 'python ./submit.py' in terminal and will connect to coursera, and the data for problems is taken from 'data' directory.

2. solver.py :
	The file that is called when submit.py is run. Constains the solver functon that returns the output data required for passing the assignment consisting of value of solution, status of optimality and the actual solution in the specified format. It calls upon two modules namely 'knapsack_greedy' and 'knapsack_dp' to solve the knapsack assignment.

3. kanpsack_greedy.py :
	The module that contains the greedy function to solve the knapsack assignment. The fourth and sixth problem are solved using greedy function.

4. knapsack_dp.py :
	The module that contains the dynamic programming approach function to solve the knapsack assignment.
