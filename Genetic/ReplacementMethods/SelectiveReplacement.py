from Genetic.Individual import *
from Genetic.ReplacementMethods import *
from Genetic.Chromosome import *


class SelectiveReplacement(BaseReplacement):

    @staticmethod
    def replace(population: [BaseIndividual], parent_1: BaseIndividual, parent_2: BaseIndividual, offspring: BaseIndividual):
        distance_to_parent_1: int = ChromosomeDistribution.distance(offspring, parent_1)
        distance_to_parent_2: int = ChromosomeDistribution.distance(offspring, parent_2)

        if parent_1.score <= offspring.score >= parent_2.score:
            if distance_to_parent_1 >= distance_to_parent_2:
                population.pop(population.index(parent_1))
                population.append(offspring)
            else:
                population.pop(population.index(parent_2))
                population.append(offspring)

        elif parent_1.score >= offspring.score >= parent_2.score or parent_1.score <= offspring.score <= parent_2.score:

            if distance_to_parent_1 >= distance_to_parent_2:
                population.pop(population.index(parent_2))
                population.append(offspring)
            else:
                population.pop(population.index(parent_1))
                population.append(offspring)

        else:
            sorted(population)
            population.pop(0)
            population.append(offspring)