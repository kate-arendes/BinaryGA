import random

GENE1LENGTH = 15
GENE2LENGTH = 20
GENE3LENGTH = 25


class Chromosome:

    # Generate initial genes

    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
        self.bitstring = ""

        for i in range(GENE1LENGTH + GENE2LENGTH + GENE3LENGTH):
            self.bitstring += str(random.randint(0, 1))

    # Replace gene values with that of another chromosome

    def chrom_copy(self, chromosome):
        self.bitstring = str(chromosome.bitstring)

    # Print a chromosome

    def print_chrom(self):
        print(self.bitstring)

    # Evaluate objective function with the given chromosome values

    def eval(self):
        gene_range = (self.max - self.min)

        float_x1 = ((int(self.bitstring[0:GENE1LENGTH], 2)) / (2 ** GENE1LENGTH - 1)) * gene_range + self.min
        float_x2 = ((int(self.bitstring[GENE1LENGTH:GENE1LENGTH + GENE2LENGTH], 2)) / (2 ** GENE2LENGTH - 1)) * gene_range + self.min
        float_x3 = ((int(self.bitstring[GENE1LENGTH + GENE2LENGTH:], 2)) / (2 ** GENE3LENGTH - 1)) * gene_range + self.min

        return float_x1**2 + float_x2**2 + float_x3**2

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
