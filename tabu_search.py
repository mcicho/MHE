from contextlib import redirect_stdout
import os
from main import *

# Tabu Search function
def tabu_search(items, bin_capacity, max_iterations, tabu_size):
    current_solution = random.sample(items, len(items))
    current_bins = solver_function(current_solution, bin_capacity)
    current_goal = goal_function(current_bins)

    best_bins = current_bins.copy()
    best_goal = current_goal

    tabu_list = []
    iteration = 0

    while iteration < max_iterations:

        neighborhood = generate_neighborhood(current_solution)
        
        # Collect neighborhood goals
        neighborhood_goals = []
        for neighbor in neighborhood:
            neighbor_bins = solver_function(neighbor, bin_capacity)
            neighbor_goal = goal_function(neighbor_bins)
            neighborhood_goals.append(neighbor_goal)

        # Check goals if are in tabu list
        best_move_index = -1
        best_move_goal = 0
        for i in range(len(neighborhood_goals)):
            if neighborhood_goals[i] < best_move_goal and neighborhood[i] not in tabu_list:
                best_move_index = i
                best_move_goal = neighborhood_goals[i]

        # Update the current solution and better solution
        if best_move_index != -1:
            current_solution = neighborhood[best_move_index]
            current_bins = solver_function(current_solution, bin_capacity)
            current_goal = goal_function(current_bins)

            if current_goal < best_goal:
                best_bins = current_bins.copy()
                best_goal = current_goal

            # Add the current move to the tabu list
            tabu_list.append(neighborhood[best_move_index])
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
        
        #print_solution(best_goal, iteration)
        iteration += 1

    return best_bins, best_goal


# # Solve using Tabu Search
# os. remove('results/ts_iter_bins.csv')
# with open('results/ts_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f): 
#         start_time = time.time()
#         tabu_search_solution, num_used_bins = tabu_search(items, bin_capacity, max_iterations, tabu_size)
#         elapsed_time = time.time() - start_time


# #os. remove('results/ts_time_bins.csv')
# with open('results/ts_time_bins.csv', 'w') as f:
#     with redirect_stdout(f): 
#         start_time = time.time()
#         tabu_search_solution, num_used_bins = tabu_search(items, bin_capacity, max_iterations, tabu_size)
#         elapsed_time = time.time() - start_time
#         print(num_used_bins, elapsed_time)


# print("Taboo Search Time:", elapsed_time, "seconds")
# print("Taboo Search Solution:", tabu_search_solution)
# print("Taboo Search Used bins:", num_used_bins,"\n")


# Time and used  bins for experiments
start_time = time.time()
tabu_search_solution, num_used_bins = tabu_search(items, bin_capacity, max_iterations, tabu_size)
elapsed_time = time.time() - start_time
print(num_used_bins, elapsed_time)