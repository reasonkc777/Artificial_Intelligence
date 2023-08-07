import random

def fitness(x):
    return x**2 + 5*x + 6

def initialize_population(pop_size, min_val, max_val):
    return [random.uniform(min_val, max_val) for _ in range(pop_size)]

def select_parents(population, num_parents):
    parents = []
    for _ in range(num_parents):
        parent = random.choice(population)
        parents.append(parent)
    return parents

def crossover(parents, num_offspring):
    offspring = []
    for _ in range(num_offspring):
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = (parent1 + parent2) / 2.0
        offspring.append(child)
    return offspring

def mutate(offspring, mutation_rate, min_val, max_val):
    mutated_offspring = []
    for child in offspring:
        if random.random() < mutation_rate:
            mutated_child = child + random.uniform(-1, 1)
            mutated_child = max(min_val, min(mutated_child, max_val))
            mutated_offspring.append(mutated_child)
        else:
            mutated_offspring.append(child)
    return mutated_offspring

def genetic_algorithm(pop_size, num_generations, num_parents, num_offspring, mutation_rate, min_val, max_val):
    population = initialize_population(pop_size, min_val, max_val)

    for generation in range(num_generations):
        print(f"Generation {generation}:")
        fitness_scores = [fitness(x) for x in population]
        best_fit = max(fitness_scores)
        best_index = fitness_scores.index(best_fit)
        print(f"Best value in generation: {population[best_index]} with fitness: {best_fit}")

        parents = select_parents(population, num_parents)
        offspring = crossover(parents, num_offspring)
        mutated_offspring = mutate(offspring, mutation_rate, min_val, max_val)

        population = mutated_offspring

    return population[best_index]


population_size = 50
num_generations = 100
num_parents = 10
num_offspring = 40
mutation_rate = 0.1
min_value = -10
max_value = 10

best_solution = genetic_algorithm(population_size, num_generations, num_parents, num_offspring, mutation_rate, min_value, max_value)
best_fitness = fitness(best_solution)

print("\nGenetic Algorithm Results:")
print(f"Best solution found: {best_solution}")
print(f"Best fitness value: {best_fitness}")
