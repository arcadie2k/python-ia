import random
import time

# Funcția de evaluare a fitnessului
def evaluate_fitness(board):
    clashes = 0
    n = len(board)

    for i in range(n):
        for j in range(i+1, n):
            # Verifică dacă există coliziuni pe aceeași linie sau pe diagonale
            if board[i] == board[j] or board[i] - board[j] == i - j or board[i] - board[j] == j - i:
                clashes += 1

    # Fitnessul este invers proporțional cu numărul de coliziuni
    fitness = 1 / (1 + clashes)
    return fitness

# Funcția de selecție a părinților utilizând turnirul binar
def select_parents(population, num_parents):
    selected_parents = []
    population_size = len(population)

    for _ in range(num_parents):
        # Selectează doi părinți aleatorii din populație
        random_indices = random.sample(range(population_size), 2)
        parent1 = population[random_indices[0]]
        parent2 = population[random_indices[1]]

        # Alege părintele cu fitnessul mai mare
        if parent1['fitness'] > parent2['fitness']:
            selected_parents.append(parent1)
        else:
            selected_parents.append(parent2)

    return selected_parents

# Funcția de încrucișare (crossover)
def crossover(parent1, parent2):
    n = len(parent1['board'])
    crossover_point = random.randint(1, n - 1)

    child1 = {'board': parent1['board'][:crossover_point] + parent2['board'][crossover_point:],
              'fitness': 0}
    child2 = {'board': parent2['board'][:crossover_point] + parent1['board'][crossover_point:],
              'fitness': 0}

    return child1, child2

# Funcția de mutație
def mutate(child, mutation_rate):
    n = len(child['board'])

    for i in range(n):
        # Aplică mutația pe fiecare genă (poziție)
        if random.random() < mutation_rate:
            child['board'][i] = random.randint(1, n)

    return child

# Funcția de rezolvare a problemei celor N regine utilizând algoritmul genetic
def solve_n_queens_ga(n, population_size, num_generations, mutation_rate):
    population = []

    # Inițializează populația inițială
    for _ in range(population_size):
        board = [random.randint(1, n) for _ in range(n)]
        fitness = evaluate_fitness(board)
        population.append({'board': board, 'fitness': fitness})

    for generation in range(num_generations):
        new_population = []

        # Selectează părinții
        parents = select_parents(population, population_size // 2)

        # Realizează încrucișarea și mutația pentru a obține copiii
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2= mutate(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)
            # Evaluează fitnessul pentru noua populație
            for individual in new_population:
                individual['fitness'] = evaluate_fitness(individual['board'])

            # Adaugă copiii în populație
            population.extend(new_population)

            # Sortează populația în funcție de fitness
            population = sorted(population, key=lambda x: x['fitness'], reverse=True)

            # Păstrează doar cei mai buni indivizi
            population = population[:population_size]

            # Verifică dacă s-a găsit o soluție
            if population[0]['fitness'] == 1:
                return population[0]['board']

        # Returnează cea mai bună soluție găsită
        return population[0]['board']
def init():   
    with open("src/input/AGqueens.txt", "r") as file:
            lines = file.readlines()
    for line in lines:
        n = int(line.strip())
        population_size = 100 # Dimensiunea populației
        num_generations = 100 # Numărul de generații
        mutation_rate = 0.01 # Rata de mutație
        start_time = time.time()
        solution = solve_n_queens_ga(n, population_size, num_generations, mutation_rate)
        print("Soluția găsită pentru problema celor", n, "regine:")
        print(solution)
        with open("src/output/AGQueens.txt", "a", encoding='utf-8') as file:
            file.write("Soluția găsită pentru problema celor " + str(n) + " regine:\n")
            file.write(str(solution))
            file.write("\n")
        end_time = time.time()
        execution_time = end_time - start_time
        with open("src/time_exec/AGQueens_time_exec.txt", 'a') as file:
            file.write(str(n)+' '+str(execution_time)+'\n')
        print(str(execution_time)+'\n')

