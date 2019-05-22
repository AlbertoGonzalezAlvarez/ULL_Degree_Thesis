from Genetic.Components import Individual
import random
import copy

class Crossover:
    CUTTING_POINTS = None

    @classmethod
    def apply(cls, individual_1: Individual, individual_2: Individual, crosspoints = []) -> [Individual]:
        if (isinstance(individual_1, Individual) and isinstance(individual_2, Individual)):
            individual_1 = individual_1.chromosome
            individual_2 = individual_2.chromosome

        if len(crosspoints) == 0:
            crosspoints = random.sample(range(0, len(individual_1)), Crossover.CUTTING_POINTS)

        father_gens = individual_1
        mother_gens = individual_2

        chromosome_offspring_1 = Crossover.__swapElements(father_gens, mother_gens, crosspoints, copy.copy(father_gens))
        chromosome_offspring_2 = Crossover.__swapElements(mother_gens, father_gens, crosspoints, copy.copy(mother_gens))

        offspring_1 = Individual(chromosome = chromosome_offspring_1)
        offspring_2 = Individual(chromosome = chromosome_offspring_2)

        return [offspring_1, offspring_2]

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

        # From last index until father or mother gens
        if switcher % 2 == 0:
            offspring[last_crosspoint_index:index] = father_gens[last_crosspoint_index:father_gens.lenght]
        else:
            offspring[last_crosspoint_index:index] = mother_gens[last_crosspoint_index:mother_gens.lenght]

        return offspring