import random

class Crossover:
    cutting_points = None

    @classmethod
    def apply(cls, chromosome1, chromosome2, crosspoints = []):
        if len(crosspoints) == 0:
            crosspoints = random.sample(range(0, len(chromosome1)), Crossover.cutting_points)

        print(crosspoints)
        father_gens = chromosome1.getChromosome()
        mother_gens = chromosome2.getChromosome()

        offspring_1 = Crossover.__swapElements(father_gens, mother_gens, crosspoints, father_gens.copy())
        offspring_2 = Crossover.__swapElements(mother_gens, father_gens, crosspoints, mother_gens.copy())

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

        return offspring