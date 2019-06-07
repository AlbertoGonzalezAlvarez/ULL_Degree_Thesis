from Genetic.Components import Individual, Chromosome
import random
import copy
from Log import LoggerHandler


class Crossover:

    @classmethod
    def apply(cls, individual_1: Individual, individual_2: Individual) -> [Individual]:
        chromosome_offspring_1 = {}
        chromosome_offspring_2 = {}

        for category in individual_1.chromosome:
            if (isinstance(individual_1, Individual) and isinstance(individual_2, Individual)):
                chromosome_individual_1 = copy.deepcopy(individual_1.chromosome[category])
                chromosome_individual_2 = copy.deepcopy(individual_2.chromosome[category])

            if len(chromosome_individual_1) < len(chromosome_individual_2):
                cross_point = random.randint(0, len(chromosome_individual_1))
            else:
                cross_point = random.randint(0, len(chromosome_individual_2))

            father_gens = copy.deepcopy(chromosome_individual_1)
            mother_gens = copy.deepcopy(chromosome_individual_2)

            partial_chromosome_offspring_1 = Crossover.__mixGens__(father_gens, mother_gens, cross_point, copy.deepcopy(father_gens))
            partial_chromosome_offspring_2 = Crossover.__mixGens__(mother_gens, father_gens, cross_point, copy.deepcopy(mother_gens))

            chromosome_offspring_1[category] = partial_chromosome_offspring_1
            chromosome_offspring_2[category] = partial_chromosome_offspring_2

            if len(chromosome_offspring_1) == 0 or len(chromosome_offspring_2) == 0:
                LoggerHandler.error(__name__, f"Error crossover")

        return [Individual(chromosome=chromosome_offspring_1), Individual(chromosome=chromosome_offspring_2)]

    @staticmethod
    def __mixGens__(father_chromosome:Chromosome, mother_chromosome: Chromosome, crosspoint: int, offspring:Chromosome) -> Chromosome:
        offspring.gens[crosspoint+1:mother_chromosome.lenght] = mother_chromosome[crosspoint+1:mother_chromosome.lenght]
        return offspring