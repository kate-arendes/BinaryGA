from Population import Population
from Chromosome import Chromosome
import random
import math
import statistics


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

    best_solutions = []
    best_f_vals = []

    overall_f_best = math.inf
    overall_best_chrom = Chromosome(0, 0)

    for i in range(30):
        random.seed(i)
        best_solutions.append(evolve(30, -7.0, 4, 50, 0.8, 0.1))
        best_f_vals.append(best_solutions[i].eval())
        if best_solutions[i].eval() < overall_f_best:
            overall_best_chrom = best_solutions[i]
            overall_f_best = best_solutions[i].eval()

    print("\nResults from Thirty Independent Runs:\n")
    print("Best: " + str(overall_f_best))
    print("Mean: " + str(statistics.mean(best_f_vals)))
    print("Stdev: " + str(statistics.stdev(best_f_vals)))

    print("\n\nBest Overall Solution\n")
    print("Chromosome: " + overall_best_chrom.bitstring)
    print("Gene Vector: ", end='')
    overall_best_chrom.print_genes()
