from Genetic.SelectionMethods import SelectionMethods
from Genetic.Components import Population
import random

class Roulette_Wheel(SelectionMethods):

    COEFFICIENT: float = 0.25

    @classmethod
    def getParents(cls, population: Population):
        accumulative_prob: list = [0]
        sorted_population = sorted(population.individuals, key = lambda individual: individual.score, reverse = True)

        for index in range(len(sorted_population)):
            accumulative_prob.append(Roulette_Wheel.COEFFICIENT * (1 - Roulette_Wheel.COEFFICIENT) ** (index - 1))

        random_number = random.uniform(0, max(accumulative_prob))

        individual = None
        for index in range(1, len(accumulative_prob)):
            if accumulative_prob[index - 1] < random_number < accumulative_prob[index]:
                index_of_parent = population.individualIndex(sorted_population[index])
                individual = population.pop(index_of_parent)

        return individual
