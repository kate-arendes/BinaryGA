# Kate Arendes - CS 5320 - Project 3 - Chromosome.py
# This file contains the Chromosome class used in the simple binary genetic algorithm in main.py

import random

# Lengths of the strings representing each gene in the chromosome

GENE1LENGTH = 15
GENE2LENGTH = 20
GENE3LENGTH = 25


# The Chromosome class represents a set of genes, or X vector, used to evaluate an objective function
class Chromosome:

    # Generate initial genes in the range minimum to maximum

    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
        self.float_x1 = 0.0
        self.float_x2 = 0.0
        self.float_x3 = 0.0
        self.bitstring = ""

        # Generate bitstring representation

        for i in range(GENE1LENGTH + GENE2LENGTH + GENE3LENGTH):
            self.bitstring += str(random.randint(0, 1))

    # Replace chromosome bit string with that of another chromosome

    def chrom_copy(self, chromosome):
        self.bitstring = str(chromosome.bitstring)

    # Prints a chromosome's bit string

    def print_chrom(self):
        print(self.bitstring)

    # Evaluate objective function with the given gene values (and simultaneously assign gene values to attributes)

    def eval(self):
        gene_range = (self.max - self.min)

        self.float_x1 = ((int(self.bitstring[0:GENE1LENGTH], 2)) / (2 ** GENE1LENGTH - 1)) * gene_range + self.min
        self.float_x2 = ((int(self.bitstring[GENE1LENGTH:GENE1LENGTH + GENE2LENGTH], 2)) / (2 ** GENE2LENGTH - 1)) \
                        * gene_range + self.min
        self.float_x3 = ((int(self.bitstring[GENE1LENGTH + GENE2LENGTH:], 2)) / (2 ** GENE3LENGTH - 1)) * gene_range \
                        + self.min

        return self.float_x1**2 + self.float_x2**2 + self.float_x3**2

    # Performs bitwise mutation with a given probability

    def mutate(self, prob_mutate):
        for i in range(len(self.bitstring)):
            if random.uniform(0, 1) < prob_mutate:
                if self.bitstring[i] == '1':
                    edited_string = list(self.bitstring)
                    edited_string[i] = '0'
                    self.bitstring = ''.join(edited_string)
                else:
                    edited_string = list(self.bitstring)
                    edited_string[i] = '1'
                    self.bitstring = ''.join(edited_string)

    # Print floating-point representations of the chromosome's gene values

    def print_genes(self):
        print("(" + str('{:.30f}'.format(self.float_x1)) + ",\n" + str('{:.30f}'.format(self.float_x2)) + ",\n" +
              str('{:.30f}'.format(self.float_x3)) + ")")
