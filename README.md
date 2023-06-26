# genetic-algorithm
For information on genetic algorithm, please see https://github.com/Ishikawa7/Quick-paths-to-start/blob/main/Genetic%20algorithms/README.md

# the problem
Given a list of products with different quantities. Find a way to put products into a van so that we maximize the total value of the van, given the constraint of the space of the van

# algorithm implementation and testing
the main algorithm is in `test_main.py`

run `pytest` to test the algorithm

# to run the simulation for the solution
- edit `products.csv` file for different configurations of the problem
- enable python virtual environment
- choose how many iterations to run and the size of the population in `main.py`
- run `python3 main.py`

Typical printout:


>Iteration 498: Avg. fitness 324.827, Best fitness 32383.7, Genome 2 2 1 2 0 1 0 1 3 9 1 0 1 1
Iteration 499: Avg. fitness 324.827, Best fitness 32383.7, Genome 2 2 1 2 0 1 0 1 3 9 1 0 1 1

The genome is the quantity of each product to be put in the van