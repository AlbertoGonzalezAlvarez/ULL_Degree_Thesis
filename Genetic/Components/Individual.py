from __future__ import annotations
from Genetic.Components import Chromosome
import random


class Individual:

    MAX_INDIVIDUAL_FEATURES = 0

    def __init__(self, lenght: int = 0, chromosome: Chromosome = None):
        if isinstance(chromosome, Chromosome):
            self.chromosome: Chromosome = chromosome
        else:
            self.chromosome: Chromosome = Chromosome(size = lenght)

        self.score: float = 0.0
        self.globalScore: float = 1.0

    @staticmethod
    def generateRandom(individual_lenght: int = 0) -> Individual:
        individual = Individual(individual_lenght)
        threshold = Individual.MAX_INDIVIDUAL_FEATURES / individual_lenght

        for index in range(individual_lenght):
            if (random.uniform(0, 1) < threshold):
                individual.chromosome.alterGen(index)

        return individual

    def __str__(self):
        return str(self.chromosome)

    def __repr__(self):
        return str(self.chromosome)

    @staticmethod
    def setMaxIndividualFeatures(maxIndividualFeatures: int) -> None:
        Individual.MAX_INDIVIDUAL_FEATURES = maxIndividualFeatures