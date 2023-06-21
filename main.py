import itertools 
import random
import sys
import time

# Read sample data from file
def data(file_path):
    items = []
    bin_capacity = None
    with open(file_path, 'r') as file:
        lines = file.readlines()
        items_line = lines[0].strip().replace(',', ' ')
        items.extend([float(item) for item in items_line.split()])
        bin_capacity = float(lines[1])

    return items, bin_capacity

file_path = 'items.txt'
items, bin_capacity = data(file_path)


# Function to pack items into bins
def solver_function(items, bin_capacity):
    bin_configuration = [0] * len(items)
    
    for item in items:
        for i in range(len(bin_configuration)):
            if bin_configuration[i] + item <= bin_capacity:
                bin_configuration[i] += item
                break
        else:
            bin_configuration.append(item)

    return bin_configuration

# Function to calculate the number of used bins
def goal_function(bin_configuration):
    num_used_bin = len([bin for bin in bin_configuration if bin > 0])
    return num_used_bin

# # Brute force function
# def brute_force(items, bin_capacity):
    
#     # Start the timer
#     start_time = time.time()

#     best_solution = None
#     best_goal = float('inf')

#     # Generate all permutations of items
#     for permutation in itertools.permutations(items):
#         bins = [0] * len(permutation)

#         # Try to pack items into bins
#         for item in permutation:
#             for i, bin in enumerate(bins):
#                 if bin + item <= bin_capacity:
#                     bins[i] += item
#                     break
#             else:
#                 bins.append(item)

#         goal = goal_function(bins)

#         # Update best solution
#         if goal < best_goal:
#             best_goal = goal
#             best_solution = bins

#      # Calculate the elapsed time
#     elapsed_time = time.time() - start_time
#     print("Brute Force Execution Time:", elapsed_time, "seconds")

#     return best_solution, best_goal

# Random hill climbing function
def random_hill_climbing(items, bin_capacity, max_iterations):
    current_solution = random.sample(items, len(items))
    current_goal = goal_function(current_solution)

    for _ in range(max_iterations):
        neighbor_bins = current_solution.copy()

        # Randomly select two items to swap
        idx1, idx2 = random.sample(range(len(items)), 2)
        neighbor_bins[idx1], neighbor_bins[idx2] = neighbor_bins[idx2], neighbor_bins[idx1]

        neighbor_solution = solver_function(neighbor_bins, bin_capacity)
        neighbor_goal = goal_function(neighbor_solution)
        # print("Neighbor configuration: ", neighbor_solution)
        # print(neighbor_goal)

        if neighbor_goal < current_goal:
            current_solution = neighbor_solution
            current_goal = neighbor_goal

    return current_solution, current_goal


# Determistic Hill Climbing function
def determistic_hill_climbing(items, bin_capacity, max_iterations):
    current_solution = random.sample(items, len(items))
    current_goal = goal_function(current_solution)

    for _ in range(max_iterations):

        # Randomly select two neighboring items
        idx1 = random.randrange(len(items) - 1)
        idx2 = idx1 + 1
        # Swap the positions of the selected items
        neighbor_bins = current_solution.copy()
        neighbor_bins[idx1], neighbor_bins[idx2] = neighbor_bins[idx2], neighbor_bins[idx1]
        
        neighbor_solution = solver_function(neighbor_bins, bin_capacity)
        neighbor_goal = goal_function(neighbor_solution)

        if neighbor_goal < current_goal:
            current_solution = neighbor_bins
            current_goal = neighbor_goal

    return current_solution, current_goal


# Function to generate neighbors
def generate_neighbors(solution):
    neighbors = []
    num_bins = len(solution)

    for i in range(num_bins):
        for j in range(i+1, num_bins):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors


# Tabu Search function
def tabu_search(items, bin_capacity, max_iterations, tabu_size):
    current_solution = random.sample(items, len(items))
    current_bins = solver_function(current_solution, bin_capacity)
    current_goal = goal_function(current_bins)

    best_solution = current_solution.copy()
    best_bins = current_bins.copy()
    best_goal = current_goal

    tabu_list = []
    iteration = 0

    while iteration < max_iterations:
        neighborhood = []
        for i in range(len(items) - 1):
            for j in range(i + 1, len(items)):
                neighbor = current_solution.copy()
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                neighborhood.append(neighbor)

        # Evaluate the solutions in the neighborhood
        neighborhood_goals = []
        for neighbor in neighborhood:
            neighbor_bins = solver_function(neighbor, bin_capacity)
            neighbor_goal = goal_function(neighbor_bins)
            neighborhood_goals.append(neighbor_goal)

        # Find the best non-tabu move
        best_move_index = -1
        best_move_goal = float('inf')
        for i in range(len(neighborhood_goals)):
            if neighborhood_goals[i] < best_move_goal and neighborhood[i] not in tabu_list:
                best_move_index = i
                best_move_goal = neighborhood_goals[i]

        # Update the current solution
        if best_move_index != -1:
            current_solution = neighborhood[best_move_index]
            current_bins = solver_function(current_solution, bin_capacity)
            current_goal = goal_function(current_bins)

            # Update the best solution if the current solution is better
            if current_goal < best_goal:
                best_solution = current_solution.copy()
                best_bins = current_bins.copy()
                best_goal = current_goal

            # Add the current move to the tabu list
            tabu_list.append(neighborhood[best_move_index])
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)

        iteration += 1

    return best_bins, best_goal

# Tabu Search function with backtrack
def tabu_search_backtrack(items, bin_capacity, max_iterations, tabu_size):
    current_solution = random.sample(items, len(items))
    current_bins = solver_function(current_solution, bin_capacity)
    current_goal = goal_function(current_bins)

    best_solution = current_solution.copy()
    best_bins = current_bins.copy()
    best_goal = current_goal

    tabu_list = []
    iteration = 0

    move_stack = []  # Stack to store the moves

    while iteration <= max_iterations:
        # Generate neighboring solutions
        neighbors = generate_neighbors(current_solution)

        best_move_index = -1
        best_neighbor = None
        best_neighbor_goal = float('inf')

        for idx, neighbor in enumerate(neighbors):
            if neighbor not in tabu_list:
                neighbor_goal = goal_function(neighbor)
                if neighbor_goal < best_neighbor_goal:
                    best_move_index = idx
                    best_neighbor = neighbor
                    best_neighbor_goal = neighbor_goal

        if best_move_index != -1:
            # Update current solution and goal
            current_solution = best_neighbor
            current_goal = best_neighbor_goal

            # Update the tabu list
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)

            # Update the best solution if necessary
            if current_goal < best_goal:
                best_solution = current_solution
                best_goal = current_goal

            # Push the move to the stack
            move_stack.append(best_neighbor)
        else:
            if move_stack:
                # Backtrack to the last available move
                current_solution = move_stack.pop()
                current_goal = goal_function(current_solution)
                tabu_list.pop()  # Remove the move from the tabu list
            else:
                break  # No improving move found and no moves to backtrack, terminate the search

        iteration += 1

    return best_bins, best_goal









# Sample data
#items = [4.5, 5.2, 2.1, 6, 3, 7, 1, 3, 5, 6, 1, 2, 4, 5, 6, 7, 8, 1, 1, 2, 5, 6]
#items = [4.5, 5.2, 2.1, 6, 3, 7, 1, 3, 5, 6, 1, 2, 4, 5, 6, 7, 8, 1, 1, 2, 5, 6, 4.5, 5.2, 2.1, 6, 3, 7, 1, 3, 5, 6, 1, 2, 4, 5, 6, 7, 8, 1, 1, 2, 5, 6]
#bin_capacity = 10.5

max_iterations = int(sys.argv[1])
tabu_size = int(sys.argv[2])


# # Solve using brute force
# brute_force_solution, num_used_bins = brute_force(items, bin_capacity)
# print("Brute Force Solution:", brute_force_solution)
# print("Brute Force Used bins:", num_used_bins)

# Solve using random hill climbing
start_time = time.time()
random_hill_climbing_solution, num_used_bins = random_hill_climbing(items, bin_capacity, max_iterations)
elapsed_time = time.time() - start_time
print("Random Hill Climbing Time:", elapsed_time, "seconds")
print("Random hill Climbing Solution:", random_hill_climbing_solution)
print("Random hill Climbing Used bins:", num_used_bins, "\n")

# Solve using Determistic Hill Climbing
start_time = time.time()
determistic_hill_climbing_solution, num_used_bins = determistic_hill_climbing(items, bin_capacity, max_iterations)
elapsed_time = time.time() - start_time
print("Determistic Hill Climbing Time:", elapsed_time, "seconds")
print("Determistic Hill Climbing Solution:", determistic_hill_climbing_solution)
print("Determistic Hill Climbing Used bins:", num_used_bins,"\n")

# Solve using Taboo Search 
start_time = time.time()
tabu_search_solution, num_used_bins = tabu_search(items, bin_capacity, max_iterations, tabu_size)
elapsed_time = time.time() - start_time
print("Taboo Search Time:", elapsed_time, "seconds")
print("Taboo Search Solution:", tabu_search_solution)
print("Taboo Search Used bins:", num_used_bins,"\n")

# Solve using Taboo Search Backtrack
start_time = time.time()
tabu_search_backtrack_solution, num_used_bins = tabu_search_backtrack(items, bin_capacity, max_iterations, tabu_size)
elapsed_time = time.time() - start_time
print("Taboo Search Backtrack Time:", elapsed_time, "seconds")
print("Taboo Search Backtrack Solution:", tabu_search_backtrack_solution)
print("Taboo Search Backtrack Used bins:", num_used_bins,"\n")
