import os
from main import *
from contextlib import redirect_stdout


# Random hill climbing function
def random_hill_climbing(items, bin_capacity, max_iterations):
    current_solution = random.choices(items, k=len(items))
    current_goal = goal_function(current_solution)

    for i in range(max_iterations):
        neighbor_configuration = current_solution.copy()

        # Select two random items and swap
        idx1, idx2 = random.sample(range(len([i for i in neighbor_configuration if i > 0])), 2)
        neighbor_configuration[idx1], neighbor_configuration[idx2] = neighbor_configuration[idx2], neighbor_configuration[idx1]
        neighbor_solution = solver_function(neighbor_configuration, bin_capacity)
        neighbor_goal = goal_function(neighbor_solution)

        # Update better solution and goal
        if neighbor_goal < current_goal:
            current_solution = neighbor_solution
            current_goal = neighbor_goal
        
        #print_solution(current_goal, i)

    return current_solution, current_goal


# Solve using random hill climbing
# os. remove('results/rhc_iter_bins.csv')
# with open('results/rhc_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f):
#         start_time = time.time()
#         random_hill_climbing_solution, num_used_bins = random_hill_climbing(items, bin_capacity, max_iterations)
#         elapsed_time = time.time() - start_time


os. remove('results/rhc_iter_bins.csv')
with open('results/rhc_iter_bins.csv', 'w') as f:
    with redirect_stdout(f):
        start_time = time.time()
        random_hill_climbing_solution, num_used_bins = random_hill_climbing(items, bin_capacity, max_iterations)
        elapsed_time = time.time() - start_time
        print(num_used_bins, elapsed_time)

#print("Random Hill Climbing Time:", elapsed_time, "seconds")
print("Random hill Climbing Solution:", random_hill_climbing_solution)
print("Random hill Climbing Used bins:", num_used_bins, "\n")


# Time and used  bins for experiments
start_time = time.time()
random_hill_climbing_solution, num_used_bins = random_hill_climbing(items, bin_capacity, max_iterations)
elapsed_time = time.time() - start_time
print(num_used_bins, elapsed_time)