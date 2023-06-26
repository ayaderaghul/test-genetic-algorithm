import random
import csv

data = []
with open('products.csv') as csv_f:
    csv_reader = csv.reader(csv_f, delimiter=',')
    for row in csv_reader:
        data.append(row)

LENGTH = 14
ITEM_QUANTITY = [int(row[3]) for row in data[1:-1]]
ITEM_SPACE = [float(row[1]) for row in data[1:-1]]
ITEM_PRICE = [float(row[2]) for row in data[1:-1]]
SPACE = 5
MAX_FITNESS = 126173.1

# BASICS
def generate_genome():
    return [random.randint(0, ITEM_QUANTITY[i]) for i in range(LENGTH)]

def test_generate_genome():
    a = generate_genome()
    assert len(a) == LENGTH
    assert all([x <= ITEM_QUANTITY[i] for i, x in enumerate(a)])

def generate_population(size):
    return [generate_genome() for _ in range(size)]

def test_generate_population():
    N = generate_population(10)
    assert len(N) == 10
    assert all([len(x) == LENGTH for x in N])
    assert all([all([y <= ITEM_QUANTITY[i] for i, y in enumerate(x)]) for x in N])

def single_point_crossover(a, b):
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")
    length = len(a)
    if length < 2:
        return a, b
    p = random.randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]

def test_single_point_crossover():
    a = generate_genome()
    b = generate_genome()
    c, d = single_point_crossover(a, b)
    assert len(c) == len(d) == len(a) == len(b)
    assert all([c[i] == a[i] or c[i] == b[i] for i in range(len(c))])
    assert all([d[i] == a[i] or d[i] == b[i] for i in range(len(d))])

def mutation(genome, num=1):
    for _ in range(num):
        index = random.randint(0, len(genome) - 1)
        genome[index] = random.randint(0, ITEM_QUANTITY[index])
    return genome

def test_mutation():
    a = generate_genome()
    b = mutation(a)
    assert len(a) == len(b)
    assert all([a[i] == b[i] or b[i] <= ITEM_QUANTITY[i] for i in range(len(a))])

# EVOLUTION
def fitness_function(genome, item_volumes=ITEM_SPACE, item_values=ITEM_PRICE, max_volume=SPACE):
    total_volume = sum(genome[i]*item_volumes[i] for i in range(len(genome)))
    total_value = sum(genome[i]*item_values[i] for i in range(len(genome)))
    
    if total_volume > max_volume:
        return 1  # This genome is not a valid solution, so its fitness is 0.
    else:
        return total_value  # The fitness is the total value of the items in the knapsack.

def test_fitness_function():
    genome = generate_genome()
    f = fitness_function(genome)
    assert f < MAX_FITNESS

def population_fitness(population):
    return [fitness_function(genome) for genome in population]

def test_population_fitness():
    population = generate_population(10)
    population_fitness(population)
    assert True  # It tests syntax errors.
    SPACE = 30
    f = population_fitness(population)
    assert all([x >= 0 and x <= MAX_FITNESS for x in f])

def selection_pair(population):
    return random.choices(
        population=population,
        weights=population_fitness(population),
        k=2
    )

def test_selection_pair():
    population = generate_population(10)
    selection_pair(population)
    assert True  # It tests syntax errors.

def sort_population_by_fitness(population):
    return sorted(population, key=fitness_function, reverse=True)

def test_sort_population_by_fitness():
    pass

def genome_to_string(genome):
    return " ".join(map(str, genome))

def print_stats(population, iteration_number):
    average_fitness = sum(population_fitness(population)) / len(population)
    sorted_population = sort_population_by_fitness(population)
    best = sorted_population[0]
    print("Iteration {}: Avg. fitness {}, Best fitness {}, Genome {}".format(
        iteration_number,
        average_fitness,
        fitness_function(best),
        genome_to_string(best)
    ))
    return best


def evolve(population, mutation_chance=0.01):
    new_population = []
    sorted_population = sort_population_by_fitness(population)
    population_size = len(population)
    # Elitism
    new_population.extend(sorted_population[0:2])
    # The rest of the population
    while len(new_population) < population_size:
        parent1, parent2 = selection_pair(sorted_population)
        child1, child2 = single_point_crossover(parent1, parent2)
        if random.random() < mutation_chance:
            child1 = mutation(child1)
            child2 = mutation(child2)
        new_population.append(child1)
        new_population.append(child2)
    return new_population[0:population_size]

ITERATION = 500
population = generate_population(100)
for i in range(ITERATION):
    evolve(population)
    print_stats(population, i)