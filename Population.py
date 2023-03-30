from Chromosome import Chromosome
import random

class Population:

    # Initialize population with specified number of chromosomes with genes in given range

    def __init__(self, size, alpha, beta):

        self.size = size
        self.alpha = alpha
        self.beta = beta

        # Lists to store initial chromosomes and chromosomes during selection process
        self.chromosomes = []
        self.selected = []
        self.to_mutate = []

        # Generates initial chromosomes for the population

        for i in range(size):
            self.chromosomes.append(Chromosome(alpha, beta))

            # Print all chromosomes in a population (for testing)

    def print_pop(self):
        for i in range(self.size):
            self.chromosomes[i].print_chrom()
            print(self.chromosomes[i].eval())
        print()

    # Prints selected chromosomes from the population (for testing)

    def print_selected(self):
        for i in range(len(self.selected)):
            self.selected[i].print_chrom()
            print(self.selected[i].eval())
        print()

    # prop_selection() performs proportional selection and roulette wheel sampling on the current population

    def prop_selection(self):
        fitnesses = []
        probabilities = []

        # Converts fitness scores for use in minimization problem

        for i in range(self.size):

            # Accounts for a divide-by-zero error

            if self.chromosomes[i].eval() == 0:
                fitnesses.append(1 / 0.000000000000000000001)
            else:
                fitnesses.append(1 / self.chromosomes[i].eval())

        # Adds together all fitness scores to be used in probabilities

        fit_sum = 0.0

        for i in range(self.size):
            fit_sum += fitnesses[i]

        # Converts fitness scores to their probabilities of being selected

        for i in range(self.size):
            fitnesses[i] = fitnesses[i] / fit_sum

        # Converts fitness scores to sum of all previous scores to make "roulette wheel" selection possible

        prob_sum = 0.0

        for i in range(self.size):
            probabilities.append(prob_sum + fitnesses[i])
            prob_sum += fitnesses[i]

        # "Spins" a hypothetical uniformly random roulette wheel to select chromosomes based on their probabilities

        for i in range(self.size):
            spin = random.uniform(0, 1)
            for j in range(self.size):
                if spin < probabilities[j]:
                    new_chrom = Chromosome(self.alpha, self.beta)
                    new_chrom.chrom_copy(self.chromosomes[j])
                    self.selected.append(new_chrom)
                    break

        # Clears the list of chromosomes in preparation for crossover

        self.chromosomes.clear()

