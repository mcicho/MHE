from contextlib import redirect_stdout
import os
from main import *

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

    while iteration < max_iterations:

        neighbors = generate_neighborhood(current_solution)

        best_move_index = -1
        best_neighbor = None
        best_neighbor_goal = 0

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

            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)

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

        #print_solution(best_goal, iteration)
        iteration += 1
        
    return best_bins, best_goal


# # Solve using Taboo Search Backtrack
# os. remove('results/tsb_iter_bins.csv')
# with open('results/tsb_iter_bins.csv', 'w') as f:
#     with redirect_stdout(f):
#         start_time = time.time()
#         tabu_search_backtrack_solution, num_used_bins = tabu_search_backtrack(items, bin_capacity, max_iterations, tabu_size)
#         elapsed_time = time.time() - start_time

# #os. remove('results/tsb_time_bins.csv')
# with open('results/tsb_time_bins.csv', 'w') as f:
#     with redirect_stdout(f): 
#         start_time = time.time()
#         tabu_search_backtrack_solution, num_used_bins = tabu_search_backtrack(items, bin_capacity, max_iterations, tabu_size)
#         elapsed_time = time.time() - start_time
#         print(num_used_bins, elapsed_time)

# tabu_search_backtrack_solution, num_used_bins = tabu_search_backtrack(items, bin_capacity, max_iterations, tabu_size)
# print("Taboo Search Backtrack Time:", elapsed_time, "seconds")
# print("Taboo Search Backtrack Solution:", tabu_search_backtrack_solution)
# print("Taboo Search Backtrack Used bins:", num_used_bins,"\n")


# Time and used  bins for experiments
start_time = time.time()
tabu_search_backtrack_solution, num_used_bins = tabu_search_backtrack(items, bin_capacity, max_iterations, tabu_size)
elapsed_time = time.time() - start_time
print(num_used_bins, elapsed_time)