from Genetic.Crossover import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from Genetic.Gen import *
import random


class FixedUniformCrossover(CrossoverTypes):

    @staticmethod
    def crossover(individual_1: BaseIndividual, individual_2: BaseIndividual, individual_type: BaseIndividual,
                  chromosome_type: BaseChromosome) -> BaseIndividual:

            offsprings_chromosome: {BaseGen} = set()
            for category in individual_2.chromosome.chromosomeCategories():
                category_len = 0
                while category_len != BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION[category] - 1:
                    max_len = BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION[category] - 1
                    offsprings_chromosome_prev_size = len(offsprings_chromosome)
                    offsprings_chromosome.add(BaseChromosome.LIST_OF_GENS[category][random.randint(0, max_len)])
                    if len(offsprings_chromosome) == offsprings_chromosome_prev_size + 1:
                        category_len += 1

            removed_gens: [BaseGen] = list(set(individual_1.chromosome.gens) - offsprings_chromosome)
            individual = individual_type(BaseChromosome(list(offsprings_chromosome), removed_gens))

            return individual

