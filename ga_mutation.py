from main import *
import random



def ga_mutation(items, bin_capacity, max_iterations, mutation_parameter, id_mutation):
    current_solution = random.sample(items, len(items))

    for i in range(max_iterations):
                
        # Mutation id = 1 = Choose random item from solution
        if id_mutation == 1:

            mutation_configuration = []
    
            for i in current_solution:
                if random.uniform(0.0, 1.0) > mutation_parameter:
                #if 1 > mutation_parameter:
                    mutation_configuration.append(random.randrange(len([i for i in current_solution])))
                else:
                    mutation_configuration.append(i)
    
            print(current_solution)
            print(mutation_configuration)
    
            if mutation_configuration == current_solution:
                print("Brak mutacji")
            else:
                print("Została dokanana mutacja")


        # Mutation id = 2 = Swap random item
        elif id_mutation == 2:
            mutation_configuration = []
            for i in current_solution:
                # if random.uniform(0.0, 1.0) > mutation_parameter:
                if 1 > mutation_parameter:
                    idx1 = i
                    idx2 = random.randrange(len([i for i in current_solution]))
                    idx1, idx2 = idx2, idx1
                    mutation_configuration.append(idx1)
                else:
                    mutation_configuration.append(i)

            print(current_solution)
            print(mutation_configuration)
    
            if mutation_configuration == current_solution:
                print("Brak mutacji")
            else:
                print("Została dokonana mutacja")


    return mutation_configuration
    

# Time and used  bins for experiments
start_time = time.time()
ga_mutation_solution = ga_mutation(items, bin_capacity, max_iterations, mutation_parameter, id_mutation)
elapsed_time = time.time() - start_time
print(elapsed_time)


