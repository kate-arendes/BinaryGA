from Population import Population
from Chromosome import Chromosome
import random





if __name__ == '__main__':

    pop = Population(5, 4.0, -7.0)
    pop.print_pop()
    pop.prop_selection()
    pop.print_selected()
    pop.crossover(0.8)
    pop.print_crossed()