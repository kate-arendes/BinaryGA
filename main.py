from Population import Population
from Chromosome import Chromosome
import random
import math
import statistics

# Number of independent rungs of the genetic algorithm

RUNS = 30


# evolve() takes all algorithm and problem parameters and runs the GA a given number of times

def evolve(members, mem_min, mem_max, generations, cross_prob, mut_prob):

    # Initializes population with given parameter value

    pop = Population(members, mem_min, mem_max)

    # Tracks the best solution and its fitness value

    best_solution = pop.get_best()
    best_fit = pop.get_best().eval()

    # Performs GA over a given number of generations

    for i in range(generations):

        # The simple genetic algorithm consists of selection, crossover, and mutation

        pop.prop_selection()
        pop.crossover(cross_prob)
        pop.mutation(mut_prob)

        # Keeps track of the best solution

        if pop.get_best().eval() < best_fit:
            best_solution = pop.get_best()
            best_fit = pop.get_best().eval()

    # The best solution found is returned

    return best_solution


if __name__ == '__main__':

    # Prompts the user for algorithm parameters

    print("\nPlease enter the following algorithm parameters:\n")

    pop_size = int(input("Population size: "))
    num_generations = int(input("Number of generations: "))
    crossover_probability = float(input("Probability that crossover will occur: "))
    mutation_probability = float(input("Probability that mutation will occur: "))

    print("\nRunning the genetic algorithm . . .\n")

    # Collects the best solution from each run and its fitness value

    best_solutions = []
    best_f_vals = []

    # Tracks the best solution over all independent runs

    overall_f_best = math.inf
    overall_best_chrom = Chromosome(0, 0)

    # Conducts independent runs

    for j in range(RUNS):

        # Seeds random so that results are reproducible

        random.seed(j)

        # Adds the best solution to the running list

        best_solutions.append(evolve(pop_size, -7.0, 4, num_generations, crossover_probability, mutation_probability))
        best_f_vals.append(best_solutions[j].eval())

        # Determines if the best solution is the overall best

        if best_solutions[j].eval() < overall_f_best:
            overall_best_chrom = best_solutions[j]
            overall_f_best = best_solutions[j].eval()

    # Prints all the results from the independent runs

    print("\n============ Results from Thirty Independent Runs ============\n")
    print("Overall Best Fitness Value: " + str('{:.30f}'.format(overall_f_best)))
    print("Mean of Best Fitness Values: " + str('{:.30f}'.format(statistics.mean(best_f_vals))))
    print("Stdev of Best Fitness Values: " + str('{:.30f}'.format(statistics.stdev(best_f_vals))))

    print("\n\n==================== Best Overall Solution ====================\n")
    print("Bit-String Chromosome:\n" + overall_best_chrom.bitstring)
    print("\nFloating-Point Gene Vector: ")
    overall_best_chrom.print_genes()
    print("\nFitness Value:\n" + str('{:.30f}'.format(overall_f_best)))
    print()
