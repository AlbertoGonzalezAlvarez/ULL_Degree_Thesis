from Genetic.Components import Individual, Chromosome
import random
import copy
from Log import LoggerHandler


class Crossover:
    CUTTING_POINTS = None

    @classmethod
    def apply(cls, individual_1: Individual, individual_2: Individual, crosspoints = []) -> [Individual]:
        chromosome_offspring_1 = {}
        chromosome_offspring_2 = {}

        for category in individual_1.chromosome:
            if (isinstance(individual_1, Individual) and isinstance(individual_2, Individual)):
                chromosome_individual_1 = copy.deepcopy(individual_1.chromosome[category])
                chromosome_individual_2 = copy.deepcopy(individual_2.chromosome[category])

            if len(crosspoints) == 0:
                if len(chromosome_individual_1) <= Crossover.CUTTING_POINTS:
                    crosspoints = random.sample(range(0, len(chromosome_individual_1)), len(chromosome_individual_1))
                else:
                    crosspoints = random.sample(range(0, len(chromosome_individual_1)), Crossover.CUTTING_POINTS)

            father_gens = copy.deepcopy(chromosome_individual_1)
            mother_gens = copy.deepcopy(chromosome_individual_2)

            partial_chromosome_offspring_1 = Crossover.__swapElements(father_gens, mother_gens, crosspoints, (father_gens))
            partial_chromosome_offspring_2 = Crossover.__swapElements(mother_gens, father_gens, crosspoints, (mother_gens))

            chromosome_offspring_1[category] = partial_chromosome_offspring_1
            chromosome_offspring_2[category] = partial_chromosome_offspring_2

            if len(chromosome_offspring_1) == 0 or len(chromosome_offspring_2) == 0:
                LoggerHandler.error(__name__, f"Error crossover")

        return [Individual(chromosome=chromosome_offspring_1), Individual(chromosome=chromosome_offspring_2)]

    @staticmethod
    def __swapElements(father_gens, mother_gens, crosspoints, offspring):
        last_crosspoint_index = 0
        switcher = 0
        for index in crosspoints:
            if switcher % 2 == 0:
                offspring[last_crosspoint_index:index] = father_gens[last_crosspoint_index:index]
            else:
                offspring[last_crosspoint_index:index] = mother_gens[last_crosspoint_index:index]

            last_crosspoint_index = index
            switcher += 1

        # From last index until father or mother gens end
        if switcher % 2 == 0:
            offspring[last_crosspoint_index:index] = father_gens[last_crosspoint_index:father_gens.lenght]
        else:
            offspring[last_crosspoint_index:index] = mother_gens[last_crosspoint_index:mother_gens.lenght]

        return offspring