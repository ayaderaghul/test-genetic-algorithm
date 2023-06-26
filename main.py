from test_main import *

ITERATION = 500
population = generate_population(100)
for i in range(ITERATION):
    evolve(population)
    print_stats(population, i)