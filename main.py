from test_main import *

ITERATION = 500
population = generate_population(100)
best_fitness = []
for i in range(ITERATION):
    new_population = evolve(population)
    best, avg = print_stats(new_population, i)
    best_fitness.append(best)
    population = new_population

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(ITERATION)
y = np.array(best_fitness)

# plt.ylim(0,np.max(y))
plt.ylim(0,MAX_FITNESS)
plt.plot(x, y)
plt.savefig('result3')
plt.show()