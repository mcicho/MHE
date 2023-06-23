from main import *

# Brute force function
def brute_force(items, bin_capacity):
    best_solution = None
    best_goal = float('inf')

    # Generate all permutations of items
    for permutation in itertools.permutations(items):
        bins = [0] * len(permutation)

        # Try to pack items into bins
        for item in permutation:
            for i, bin in enumerate(bins):
                if bin + item <= bin_capacity:
                    bins[i] += item
                    break
            else:
                bins.append(item)

        goal = goal_function(bins)

        # Update best solution
        if goal < best_goal:
            best_goal = goal
            best_solution = bins

    return best_solution, best_goal

# Solve using brute force
brute_force_solution, num_used_bins = brute_force(items, bin_capacity)
print("Brute Force Solution:", brute_force_solution)
print("Brute Force Used bins:", num_used_bins)
