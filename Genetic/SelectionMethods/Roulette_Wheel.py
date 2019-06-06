from Genetic.SelectionMethods import SelectionMethods
from Genetic.Components import Individual
import random

class Roulette_Wheel(SelectionMethods):

    COEFFICIENT: float = 0.25

    @classmethod
    def getParents(cls, population: [Individual]):
        accumulative_prob: list = [0]
        population.sort(key=lambda individual: individual.score, reverse=True)

        for index in range(len(population)):
            accumulative_prob.append(Roulette_Wheel.COEFFICIENT * (1 - Roulette_Wheel.COEFFICIENT) ** (index - 1))

        random_number = random.uniform(0, max(accumulative_prob))

        individual = None
        for index in range(1, len(accumulative_prob)):
            if accumulative_prob[index - 1] < random_number < accumulative_prob[index]:
                index_of_parent = population.index(population[index])
                individual = population.pop(index_of_parent)

        return individual
