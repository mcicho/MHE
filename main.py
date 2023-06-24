from contextlib import redirect_stdout
import itertools 
import random
import sys
import time
import csv
from matplotlib import pyplot as plt
from sklearn.compose import ColumnTransformer


# Read sample data from file
def data(file_path):
    items = []
    bin_capacity = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        items_line = lines[0].strip().replace(',', ' ')
        items.extend([float(item) for item in items_line.split()])
        bin_capacity = float(lines[1])

    return items, bin_capacity

file_path = 'items/items.txt'  # small package
# file_path = 'items/items1.txt'  # bigger package
## file_path = 'items/items2.txt'  # bigger package with small ints
# file_path = 'items/items3.txt'  # huge package with small ints
items, bin_capacity = data(file_path)


# # Read parameters from terminal
# if len(sys.argv) == 2:
#     max_iterations = int(sys.argv[1])
# elif len(sys.argv) == 3: 
#     max_iterations = int(sys.argv[1])
#     tabu_size = int(sys.argv[2])
# else:
#     max_iterations = int(sys.argv[1])
#     tabu_size = int(sys.argv[2])
#     temp = float(sys.argv[3])
#     cooling_rate = float(sys.argv[4])
#     mutation_parameter = float(sys.argv[5])

if len(sys.argv) == 4: 
    max_iterations = int(sys.argv[1])
    mutation_parameter = float(sys.argv[2])
    id_mutation = int(sys.argv[3])

# Function to pack items into bins
def solver_function(items, bin_capacity):
    bin_configuration = [] * len(items)
    
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


# Function to generate close neighborhood
def generate_neighborhood(solution):
    neighborhood = []
    for i in range(len(items) - 1):
        for j in range(i + 1, len(items)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighborhood.append(neighbor)

    return neighborhood



# Function to print goals/solutions and iterations
def print_solution(goal, iteration):
    print(iteration, goal)

# Dot plot with Number of used bins vs Elapsed time
with open('results/results4.txt', 'r') as file:
    data = file.readlines()

colors = []
x_values = []
y_values = []

for row in data:
    values = row.strip().split(' ')
    colors.append(values[0])
    x_values.append(int(values[1]))
    y_values.append(float(values[2]))

color_mapping = {
    'random_hill_climbing': 'red',
    'hill_climbing': 'green',
    'tabu_search': 'blue',
    'tabu_search_backtrack': 'orange',
    'simulated_annealing': 'purple'
}

plt.scatter(x_values, y_values, c=[color_mapping[color] for color in colors])
plt.xlabel('Number of used bins')
plt.ylabel('Elapsed time')
plt.title('Number of used bins vs Elapsed time')
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='random_hill_climbing', markerfacecolor='red', markersize=7),
                   plt.Line2D([0], [0], marker='o', color='w', label='hill_climbing', markerfacecolor='green', markersize=7),
                   plt.Line2D([0], [0], marker='o', color='w', label='tabu_search', markerfacecolor='blue', markersize=7),
                   plt.Line2D([0], [0], marker='o', color='w', label='tabu_search_backtrack', markerfacecolor='orange', markersize=7),
                   plt.Line2D([0], [0], marker='o', color='w', label='simulated_annealing', markerfacecolor='purple', markersize=7)]
plt.legend(handles=legend_elements, loc='upper right')
#plt.show()





