# Kate Arendes - CS 5320 - Project 3 - Population.py
# This file contains the Population class to manage Chromosomes for the simple binary genetic algorithm in main.py

from Chromosome import Chromosome
import random
import math


# Population holds a given number of chromosomes

class Population:

    # Initialize population with specified number of chromosomes with genes in given range

    def __init__(self, size, alpha, beta):

        self.size = size
        self.alpha = alpha
        self.beta = beta

        # Lists to store initial chromosomes and chromosomes during execution of the GA

        self.chromosomes = []
        self.selected = []
        self.to_mutate = []

        # Generates initial chromosomes for the population

        for i in range(size):
            self.chromosomes.append(Chromosome(alpha, beta))

    # get_best() returns the chromosome with the best fitness value in the population

    def get_best(self):
        f_best = math.inf
        best_chrom = Chromosome(0, 0)
        for i in range(self.size):
            if self.chromosomes[i].eval() < f_best:
                f_best = self.chromosomes[i].eval()
                best_chrom = self.chromosomes[i]
        return best_chrom

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

    # crossover() takes a probability of crossover and uses the value to determine if two chromosomes will be crossed

    def crossover(self, prob_c):

        # Picks pairs of chromosomes and performs crossover

        iterations = int(self.size / 2)

        # When two chromosomes are picked, they are removed from the selected list

        for i in range(iterations):
            index1 = random.randint(0, (len(self.selected) - 1))
            chrom1 = self.selected[index1]
            del self.selected[index1]

            index2 = random.randint(0, (len(self.selected) - 1))
            chrom2 = self.selected[index2]
            del self.selected[index2]

            # Calculates whether crossover occurs and if so, performs the crossover using gene_swap()

            if random.uniform(0, 1) < prob_c:

                self.gene_swap(chrom1, chrom2)

            # Adds the crossed chromosomes back into the population's chromosome list

            self.to_mutate.append(chrom1)
            self.to_mutate.append(chrom2)

        # If there's an odd population size, the last chromosome is added to the list of chromosomes to be mutated

        if self.selected:
            self.to_mutate.append(self.selected[0])

    # gene_swap() performs a gene swap operation for two chromosomes starting at a randomized point

    def gene_swap(self, first_chrom, second_chrom):

        # Generate crossover point

        point = random.randint(1, len(first_chrom.bitstring) - 1)

        # Create resulting child bit strings

        child1 = (first_chrom.bitstring[0:point] + second_chrom.bitstring[point:])
        child2 = (second_chrom.bitstring[0:point] + first_chrom.bitstring[point:])

        # Replace parental bit strings with children's bit string

        first_chrom.bitstring = child1
        second_chrom.bitstring = child2

    # mutation() calls mutation() method of each chromosome with a given probability of mutation

    def mutation(self, prob_m):
        for i in range(len(self.to_mutate)):
            self.to_mutate[i].mutate(prob_m)
            self.chromosomes.append(self.to_mutate[i])
        self.to_mutate.clear()
