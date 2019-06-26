from Genetic.Individual import *
from Genetic.ReplacementMethods import *
from Genetic.Chromosome import *


class ReplaceWorst(BaseReplacement):

    @staticmethod
    def replace(population: [BaseIndividual], parent_1: BaseIndividual, parent_2: BaseIndividual, offspring_1: BaseIndividual, offspring_2: BaseIndividual):
        population: [BaseIndividual] = sorted(population)
        population.pop(0)
        population.append(offspring_1)

        return population