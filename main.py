from Population import Population
import random

if __name__ == '__main__':
    pop = Population(5, 4.0, -7.0)
    pop.print_pop()
    pop.prop_selection()
    pop.print_selected()
