from Genetic.Crossover import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from Genetic.Gen import *
import random


class TestCrossover(CrossoverTypes):

    @staticmethod
    def crossover(individual_1: BaseIndividual, individual_2: BaseIndividual, individual_type: BaseIndividual,
                  chromosome_type: BaseChromosome) -> BaseIndividual:

            parents_chromosomes: [] = individual_2.chromosome.selected_gens + individual_1.chromosome.selected_gens

            offsprings_chromosome: {BaseGen} = set()
            min_size = min(individual_1.chromosome.selected_gens_size, individual_2.chromosome.selected_gens_size)
            max_size = max(individual_1.chromosome.selected_gens_size, individual_2.chromosome.selected_gens_size)

            new_size = random.randint(min_size, max_size)
            while len(offsprings_chromosome) != new_size:
                offsprings_chromosome.add(parents_chromosomes[random.randint(0, (len(parents_chromosomes) - 1))])

            removed_gens: [BaseGen] = list(set(individual_1.chromosome.gens) - offsprings_chromosome)
            return individual_type(BaseChromosome(list(offsprings_chromosome), removed_gens))


