from __future__ import annotations
from Genetic.Chromosome import Chromosome
import random


class Individual:

    MAX_INDIVIDUAL_FEATURES = 0

    def __init__(self, lenght: int = 0) -> None:
        self.chromosome = Chromosome(size = lenght)
        self.score = 0

    @staticmethod
    def generateRandom(lenght: int = 0) -> Individual:
        individual = Individual(lenght)
        threshold = individual.chromosome.getSelectedFeaturesSize() / Individual.MAX_INDIVIDUAL_FEATURES

        for gen in individual.chromosome:
            print(gen)
            # if (random.uniform(0, 1) < 0.001):
            #     gen.selectGen()

        return individual

