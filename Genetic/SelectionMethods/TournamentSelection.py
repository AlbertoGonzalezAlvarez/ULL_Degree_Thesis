from Genetic.SelectionMethods import SelectionMethods
from Genetic.Components import Individual
import random

class TournamentSelection(SelectionMethods):

    COEFFICIENT: float = 0.25
    LAST_PARENT: Individual = None

    @classmethod
    def getParents(cls, population: [Individual]):
        n_of_parents = 4

        candidates = []

        for _ in range(4):
            candidates.append(population[random.randint(0, n_of_parents)])

        candidates.sort(key=lambda individual: individual.score, reverse=True)

        return candidates[0]
