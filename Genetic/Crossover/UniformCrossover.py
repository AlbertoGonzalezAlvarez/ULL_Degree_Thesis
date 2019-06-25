from Genetic.Crossover import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from Genetic.Gen import *
import random


class UniformCrossover(BaseCrossover):

    @staticmethod
    def crossover(individual_1: BaseIndividual, individual_2: BaseIndividual, individual_type: BaseIndividual,
                  chromosome_type: BaseChromosome, crossover_prob: float) -> BaseIndividual:

        if random.random() < crossover_prob:
            parents_chromosomes: [] = individual_2.chromosome.selected_gens + individual_1.chromosome.selected_gens
            random.shuffle(parents_chromosomes)

            offsprings_chromosome: {BaseGen} = {}
            min_chromosome_size: int = min(individual_1.chromosome.selected_gens_size,
                                           individual_2.chromosome.selected_gens_size)

            index: int = 0
            while len(offsprings_chromosome) != min_chromosome_size:
                offsprings_chromosome.add(parents_chromosomes[index])
                index += 1

            removed_gens: [BaseGen] = list(set(individual_1.chromosome.gens) - offsprings_chromosome)
            return individual_type(BaseChromosome(list(offsprings_chromosome), removed_gens))

        else:
            return None


