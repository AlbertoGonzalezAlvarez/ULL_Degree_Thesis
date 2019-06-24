from Genetic.Crossover import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from Genetic.Gen import *
import random


class UniformCrossover(BaseCrossover):

    @staticmethod
    def crossover(individual_1: BaseIndividual, individual_2: BaseIndividual, individual_type: BaseIndividual,
                  crossover_prob: float) -> BaseIndividual:

        if random.random() < crossover_prob:
            parents_chromosomes: BaseChromosome = individual_2.chromosome + individual_1.chromosome
            parents_chromosomes: BaseChromosome = random.shuffle(parents_chromosomes)

            offsprings_chromosome: [BaseGen] = []
            for index in range(len(parents_chromosomes)):
                offsprings_chromosome.append(parents_chromosomes[index])

            return individual_type(offsprings_chromosome)

        else:
            return None


