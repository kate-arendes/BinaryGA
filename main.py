from Population import Population
from Chromosome import Chromosome
import random
import math
import statistics

RUNS = 30


def evolve(members, mem_min, mem_max, generations, cross_prob, mut_prob):
    pop = Population(members, mem_min, mem_max)

    best_solution = pop.get_best()
    best_fit = pop.get_best().eval()

    for i in range(generations):

        # The simple genetic algorithm consists of selection, crossover, and mutation

        pop.prop_selection()
        pop.crossover(cross_prob)
        pop.mutation(mut_prob)

        # Keeps track of the best solution including its X vector, the value of its objective function, and generation

        if pop.get_best().eval() < best_fit:
            best_solution = pop.get_best()
            best_fit = pop.get_best().eval()

    return best_solution


if __name__ == '__main__':

    print("\nPlease enter the following algorithm parameters:\n")

    pop_size = int(input("Population size: "))
    num_generations = int(input("Number of generations: "))
    crossover_probability = float(input("Probability that crossover will occur: "))
    mutation_probability = float(input("Probability that mutation will occur: "))

    print("\nRunning the genetic algorithm . . .\n")

    best_solutions = []
    best_f_vals = []

    overall_f_best = math.inf
    overall_best_chrom = Chromosome(0, 0)

    for j in range(RUNS):
        random.seed(j)
        best_solutions.append(evolve(pop_size, -7.0, 4, num_generations, crossover_probability, mutation_probability))
        best_f_vals.append(best_solutions[j].eval())
        if best_solutions[j].eval() < overall_f_best:
            overall_best_chrom = best_solutions[j]
            overall_f_best = best_solutions[j].eval()

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
