import numpy

def cal_pop_fitness(equation_inputs, pop):
    fitness = numpy.sum(pop*equation_inputs, axis=1)
    return fitness

def select_mating_pool(pop, fitness, num_parents):
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parents_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parents_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    crossover_point = numpy.uint8(numpy.random.randint(1, offspring_size[1]-1))

    for k in range(offspring_size[0]):
        parent1_idx = k%parents.shape[0]
        parent2_idx = (k + 1)%parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    m_ptr = numpy.uint8(numpy.random.randint(0, offspring_crossover.shape[1] - 1))
    for idx in range(offspring_crossover.shape[0]):
        random_value = numpy.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, m_ptr] = offspring_crossover[idx, m_ptr] + random_value
    return offspring_crossover


equation_inputs = [4, -1, 3.1, 4, -6, -4.5]
num_weights = 6

sol_per_pop = 8
num_parents_mating = 4

pop_size = (sol_per_pop, num_weights)
new_population = numpy.random.uniform(low= -4.0, high=4.0, size=pop_size)
print(new_population)

num_generations = 10
for generation in range(num_generations):
    fitness = cal_pop_fitness(equation_inputs, new_population)
    parents = select_mating_pool(new_population, fitness, num_parents_mating)
    offspring_crossover = crossover(parents, offspring_size=(pop_size[0]-parents.shape[0], num_weights))
    offspring_mutation = mutation(offspring_crossover)

    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    print("세대 :", generation, " => best 해 : ", numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))


fitness = cal_pop_fitness(equation_inputs, new_population)
best_match_idex = numpy.where(fitness == numpy.max(fitness))

print("최적해 : ", new_population[best_match_idex, :])
print("최적해의 적합도 : ", fitness[best_match_idex])