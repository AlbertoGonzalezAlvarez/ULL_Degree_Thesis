from Genetic.Gen import *
from Genetic.ParentSelector import *
import random

class RouletteWheel(ParentSelector):

    COEFFICIENT: float = 0.25

    @staticmethod
    def select_parent(population: [BaseGen]):
        accumulative_prob: list = [0]
        sorted_population: [BaseGen] = sorted(population)

        for index in range(len(population)):
            accumulative_prob.append(RouletteWheel.COEFFICIENT * (1 - RouletteWheel.COEFFICIENT) ** (index - 1))

        random_number = random.uniform(0, max(accumulative_prob))

        individual = None

        if len(population) > 1:
            for index in range(1, len(accumulative_prob)):
                if accumulative_prob[index - 1] < random_number < accumulative_prob[index]:
                    index_of_parent = population.index(population[index])
                    individual = population.pop(index_of_parent)
        else:
            individual = population.pop(0)

        return individual