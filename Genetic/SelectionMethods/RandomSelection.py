from Genetic.SelectionMethods import SelectionMethods
from Genetic.Components import Individual
import random

class RandomSelection(SelectionMethods):

    COEFFICIENT: float = 0.25
    LAST_PARENT: Individual = None

    @classmethod
    def getParents(cls, population: [Individual]):

        index = random.randint(0, len(population)-1)
        print(index)
        return population[index]
