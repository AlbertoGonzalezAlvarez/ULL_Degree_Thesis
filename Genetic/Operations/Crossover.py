import random
import copy

class Crossover:
    cutting_points = None

    @classmethod
    def apply(cls, chromosome1, chromosome2, crosspoints = []):
        if len(crosspoints) == 0:
            crosspoints = random.sample(range(0, len(chromosome1)), Crossover.cutting_points)

        father_gens = chromosome1
        mother_gens = chromosome2

        offspring_1 = Crossover.__swapElements(father_gens, mother_gens, crosspoints, copy.copy(father_gens))
        offspring_2 = Crossover.__swapElements(mother_gens, father_gens, crosspoints, copy.copy(mother_gens))

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