import random

LENGTH = 14
MAX_VALUES = [3, 2, 5, 5, 5, 4, 12, 7, 7, 9, 4, 2, 6, 6]  # Customize this list based on your requirements.

def generate_genome(length=LENGTH, max_values=MAX_VALUES):
    return [random.randint(0, max_values[i]) for i in range(length)]

# Example usage:
genome = generate_genome()
print(genome)

def generate_population(size, genome_length=LENGTH, max_values=MAX_VALUES):
    return [generate_genome(genome_length, max_values) for _ in range(size)]

def single_point_crossover(a, b):
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")
    length = len(a)
    if length < 2:
        return a, b
    p = random.randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]