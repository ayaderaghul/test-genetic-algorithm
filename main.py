from test_main import *

ITERATION = 500
population = generate_population(100)
best_fitness = []
for i in range(ITERATION):
    new_population = evolve(population)
    best = print_stats(new_population, i)
    f = fitness_function(best)
    best_fitness.append(f)

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(ITERATION)
y = np.array(best_fitness)

plt.plot(x, y)
plt.savefig('result')
plt.show()