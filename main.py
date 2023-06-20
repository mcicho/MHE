import random
import itertools
import time

# Function to pack items into bins
def solver_function(items, bin_capacity):
    bins = [0] * len(items)
    
    for item in items:
        for i, bin in enumerate(bins):
            if bin + item <= bin_capacity:
                bins[i] += item
                break
        else:
            bins.append(item)
    return bins


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
    # best_solution = current_solution
    # best_goal = current_goal

    for _ in range(max_iterations):
        neighbor = current_solution.copy()

        # Randomly select two items to swap
        idx1, idx2 = random.sample(range(len(items)), 2)
        neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

        # Calculate bins configuration - solution
        neighbor_bins = solver_function(neighbor, bin_capacity)
        neighbor_goal = goal_function(neighbor_bins)
        # print("Neighbor configuration: ", neighbor)
        # print(neighbor_goal)

        # Move to the neighboring solution if it improves the goal function
        if neighbor_goal < current_goal:
            current_solution = neighbor_bins
            current_goal = neighbor_goal

            # # Update the best solution if applicable
            # if current_goal < best_goal:
            #     best_solution = current_solution
            #     best_goal = current_goal

    return current_solution, current_goal


# Classic Hill Climbing function
def classic_hill_climbing(items, bin_capacity, max_iterations):
    current_solution = random.sample(items, len(items))
    current_goal = goal_function(current_solution)
    

    for _ in range(max_iterations):

        # Randomly select two neighboring items
        idx1 = random.randrange(len(items) - 1)
        idx2 = idx1 + 1
        # Swap the positions of the selected items
        neighbor = current_solution.copy()
        neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]
        
        # Calculate bins configuration - solution
        neighbor_bins = solver_function(neighbor, bin_capacity)
        neighbor_goal = goal_function(neighbor_bins)

        # Move to the neighboring solution if it improves the goal function
        if neighbor_goal < current_goal:
            current_solution = neighbor_bins
            current_goal = neighbor_goal

    return current_solution, current_goal









# Sample data
items = [4, 5, 2, 6, 3, 7, 1, 3, 5, 6, 1, 2, 4, 5, 6, 7, 8, 1, 1, 2, 5, 6]
bin_capacity = 10
max_iterations = 100

# # Solve using brute force
# brute_force_solution, num_used_bins = brute_force(items, bin_capacity)
# print("Brute Force Solution:", brute_force_solution)
# print("Brute Force Used bins:", num_used_bins)

# Solve using random hill climbing
start_time = time.time()
random_hill_climbing_solution, num_used_bins = random_hill_climbing(items, bin_capacity, max_iterations)
elapsed_time = time.time() - start_time
print("Random Hill Climbing Execution Time:", elapsed_time, "seconds")
print("Random hill Climbing Solution:", random_hill_climbing_solution)
print("Random hill Climbing Used bins:", num_used_bins)

# Solve using Classic Hill Climbing
start_time = time.time()
classic_hill_climbing_solution, num_used_bins = classic_hill_climbing(items, bin_capacity, max_iterations)
elapsed_time = time.time() - start_time
print("Classic Hill Climbing Execution Time:", elapsed_time, "seconds")
print("Classic Hill Climbing Solution:", classic_hill_climbing_solution)
print("Classic Hill Climbing Used bins:", num_used_bins)

