import random

LENGTH = 14
MAX_VALUES = [3, 2, 5, 5, 5, 4, 12, 7, 7, 9, 4, 2, 6, 6]  # Customize this list based on your requirements.
SPACE = 5
MAX_FITNESS = 126173.1

def generate_genome(length=LENGTH, max_values=MAX_VALUES):
    return [random.randint(0, max_values[i]) for i in range(length)]

def test_generate_genome():
    a = generate_genome()
    assert len(a) == LENGTH
    assert all([x <= MAX_VALUES[i] for i, x in enumerate(a)])

def generate_population(size, genome_length=LENGTH, max_values=MAX_VALUES):
    return [generate_genome(genome_length, max_values) for _ in range(size)]

def test_generate_population():
    N = generate_population(10)
    assert len(N) == 10
    assert all([len(x) == LENGTH for x in N])
    assert all([all([y <= MAX_VALUES[i] for i, y in enumerate(x)]) for x in N])

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

def mutation(genome, num=1, max_values=MAX_VALUES):
    for _ in range(num):
        index = random.randint(0, len(genome) - 1)
        genome[index] = random.randint(0, max_values[index])
    return genome

def test_mutation():
    a = generate_genome()
    b = mutation(a)
    assert len(a) == len(b)
    assert all([a[i] == b[i] or b[i] <= MAX_VALUES[i] for i in range(len(a))])

def population_fitness(population):
    return [fitness(genome) for genome in population]
