# genetic-algorithm
For information on genetic algorithm, please see https://github.com/Ishikawa7/Quick-paths-to-start/blob/main/Genetic%20algorithms/README.md

# the problem
Given a list of products with different quantities. Find a way to put products into a van so that we maximize the total value of the van, given the constraint of the space of the van

# algorithm implementation and testing
the main algorithm is in `test_main.py`

run `pytest` to test the algorithm

# to run the simulation for the solution
- (optional) edit `products.csv` file for different configurations of the problem
- enable python virtual environment
- (optional) choose how many iterations to run and the size of the population in `main.py`, the default is 500 iterations and a population of 100 agents
- run `python3 main.py`

Typical printout:


>Iteration 498: Avg. fitness 305.2874, Best fitness 30429.739999999998, Genome 1 2 1 0 0 2 2 5 5 8 0 1 0 2

> Iteration 499: Avg. fitness 491.0916, Best fitness 49010.16, Genome 0 2 0 4 4 2 1 5 6 7 0 1 0 1

The genome is the quantity of each product to be put in the van

Best fitness overtime is in `result.png`

<img src="https://github.com/ayaderaghul/test-genetic-algorithm/blob/main/result2.png">