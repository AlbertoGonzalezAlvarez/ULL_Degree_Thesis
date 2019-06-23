from Genetic.Chromosome import *
from Genetic.Gen import *
from Genetic.Individual import *
from Genetic.IndividualGenerators import *


class FixedSize(PopulationGenerator):

    @staticmethod
    def generate_individuals(individual_type: BaseIndividual, chromosome_type: BaseChromosome,
                             list_of_gens_per_category: dict, population_size: int, category_lenghts: dict,
                             percentage_of_features: int = -1):
        pass