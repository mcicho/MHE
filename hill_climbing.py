from contextlib import redirect_stdout
import os
import random
import time
from main import *

# Determistic Hill Climbing function
def hill_climbing(items, bin_capacity, max_iterations):
    current_solution = random.sample(items, len(items))
    #current_solution = random.choices(items, k=len(items))
    current_bins = solver_function(current_solution, bin_capacity)
    current_goal = goal_function(current_bins)

    for i in range(max_iterations):
        neighbor_configuration = current_solution.copy()

        # Select two neighboring items and swap
        idx1 = random.randrange(len([i for i in neighbor_configuration if i > 0]) - 1)
        #idx1 = random.randrange(len(items) - 1)
        idx2 = idx1 + 1
        neighbor_configuration[idx1], neighbor_configuration[idx2] = neighbor_configuration[idx2], neighbor_configuration[idx1]

        neighbor_solution = solver_function(neighbor_configuration, bin_capacity)
        neighbor_goal = goal_function(neighbor_solution)
        
        # Update better solution and goal        
        if neighbor_goal < current_goal:
            current_bins = neighbor_solution
            current_goal = neighbor_goal        

        #print_solution(current_goal, i)

    return current_bins, current_goal


# # Solve using Determistic Hill Climbing
# os. remove('results/hc_iter_bins.csv')
# with open('results/hc_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f):
#         start_time = time.time()
#         hill_climbing_solution, num_used_bins = hill_climbing(items, bin_capacity, max_iterations)
#         elapsed_time = time.time() - start_time


# #os. remove('results/hc_iter_bins.csv')
# with open('results/hc_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f):
#         start_time = time.time()
#         hill_climbing_solution, num_used_bins = hill_climbing(items, bin_capacity, max_iterations)
#         elapsed_time = time.time() - start_time
#         print(num_used_bins, elapsed_time)


# print("Determistic Hill Climbing Time:", elapsed_time, "seconds")
# print("Determistic Hill Climbing Solution:", hill_climbing_solution)
# print("Determistic Hill Climbing Used bins:", num_used_bins,"\n")


# Time and used  bins for experiments
start_time = time.time()
hill_climbing_solution, num_used_bins = hill_climbing(items, bin_capacity, max_iterations)
elapsed_time = time.time() - start_time
print(num_used_bins, elapsed_time)
