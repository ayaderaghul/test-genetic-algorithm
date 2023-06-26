import pygad
import numpy
capacity = 1

# Here you define the fitness function.
def fitness_func(solution, solution_idx):
    weight = numpy.sum(solution*weights)
    value = numpy.sum(solution*values)
    if weight > capacity:
        return 0  # If weight is more than capacity return 0 (not feasible solution)
    return value

# Define the parameters of the GA
ga_instance = pygad.GA(num_generations=100,
                       num_parents_mating=5,
                       fitness_func=fitness_func,
                       sol_per_pop=10,
                       num_genes=len(weights),
                       gene_type=int,
                       init_range_low=0,
                       init_range_high=5,
                       parent_selection_type="rws",
                       keep_parents=2,
                       mutation_percent_genes=10)

# Run the GA
ga_instance.run()

# Get the solution of the problem
solution, solution_fitness, _ = ga_instance.best_solution()

# Print the best solution
print("Best solution : ", solution)
print("Best solution fitness : ", solution_fitness)
