from __future__ import annotations
from Genetic.Chromosome import Chromosome
import random


class Individual:

    MAX_INDIVIDUAL_FEATURES = 0

    def __init__(self, lenght: int = 0):
        self.chromosome: Chromosome = Chromosome(size = lenght)
        self.score: float = 0.0

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

    def calculateIndividualScore(self) -> None:
        pass

    # @staticmethod
    # def getWordsFromChromosome(chromosome: Chromosome, category_corpus: DataCategories):
    #     vect_of_words = []
    #
    #     for word_index in chromosome:
    #         vect_of_words.append(category_corpus[word_index])
    #
    #     return vect_of_words