from __future__ import annotations
from Genetic.Chromosome import Chromosome
import random


class Individual:

    MAX_INDIVIDUAL_FEATURES = 0

    def __init__(self, lenght: int = 0) -> None:
        self.chromosome = Chromosome(size = lenght)
        self.score = 0

    @staticmethod
    def generateRandom(individual_lenght: int = 0) -> Individual:
        individual = Individual(individual_lenght)
        threshold = Individual.MAX_INDIVIDUAL_FEATURES / individual_lenght

        for index in range(individual.chromosome.lenght):
            if (random.uniform(0, 1) < threshold):
                individual.chromosome.addFeatureAt(index)

        return individual

