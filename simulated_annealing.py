from main import *

import random
import math

def simulated_annealing(items, bin_capacity, max_iterations, temperature, cooling_rate):
    current_solution = random.sample(items, len(items))
    current_goal = goal_function(current_solution)
    best_solution = current_solution.copy()
    best_goal = goal_function(best_solution)

    current_temperature = temperature

    for i in range(max_iterations):

        # neighbor_solution = generate_neighborhood(current_solution)
        # neighbor_goal = goal_function(neighbor_solution)
        
        neighbor_configuration = current_solution.copy()

        # Select two random items and swap
        # idx1, idx2 = random.sample(range(len([i for i in current_solution if i > 0])), 2)
        # neighbor_configuration[idx1], neighbor_configuration[idx2] = neighbor_configuration[idx2], neighbor_configuration[idx1]
        idx1, idx2 = random.sample(range(len([i for i in neighbor_configuration if i > 0])), 2)
        neighbor_configuration = current_solution.copy()
        neighbor_configuration[idx1], neighbor_configuration[idx2] = neighbor_configuration[idx2], neighbor_configuration[idx1]
        
        neighbor_solution = solver_function(neighbor_configuration, bin_capacity)
        neighbor_goal = goal_function(neighbor_solution)
        
        # Calculate possibility to accept new solution
        possibility = math.exp((neighbor_goal - current_goal) / current_temperature)
        
        # Determine whether to accept the neighbor solution
        if neighbor_goal < current_goal or random.random() < possibility:
            current_solution = neighbor_solution.copy()
        
        # Update better solution and goal
        if neighbor_goal < best_goal:
            best_solution = neighbor_solution.copy()
            best_goal = neighbor_goal
        
        # Cool down the temperature
        current_temperature *= cooling_rate
    
    return best_solution, neighbor_goal


# Solve using simulated annealing
# os. remove('results/rhc_iter_bins.csv')
# with open('results/rhc_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f):
#         start_time = time.time()
#         simulated annealing_solution, num_used_bins = simulated annealing(items, bin_capacity, max_iterations, temp, cooling_rate)
#         elapsed_time = time.time() - start_time


# #os. remove('results/rhc_iter_bins.csv')
# with open('results/rhc_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f):
#         start_time = time.time()
#         simulated annealing_solution, num_used_bins = simulated annealing(items, bin_capacity, max_iterations, temp, cooling_rate)
#         elapsed_time = time.time() - start_time
#         print(num_used_bins, elapsed_time)
#         

# simulated_annealing_solution, num_used_bins = simulated_annealing(items, bin_capacity, max_iterations, temp, cooling_rate)
# #print("Simulated Annealing Time:", elapsed_time, "seconds")
# print("Simulated Annealing Solution:", simulated_annealing_solution)
# print("Simulated Annealing Used bins:", num_used_bins, "\n")

# Time and used  bins for experiments
start_time = time.time()
simulated_annealing_solution, num_used_bins = simulated_annealing(items, bin_capacity, max_iterations, temp, cooling_rate)
elapsed_time = time.time() - start_time
print(num_used_bins, elapsed_time)