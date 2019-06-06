from __future__ import annotations
from Genetic.Components import Chromosome
from Genetic.Fitness import TFIDF, Model_Goodness
import random


class Individual:

    MAX_INDIVIDUAL_FEATURES = 0

    def __init__(self, chromosome: Chromosome = None, category_lenghts: dict = {}):
        self.score: float = 0.0

        if chromosome != None:
            self.chromosome = chromosome
        else:
            self.chromosome = {}

            for category in category_lenghts:
                self.chromosome[category] = Chromosome(size=category_lenghts[category])

    def calculateScore(self, data: list[DataCategory]):
        individual_words = {}

        for dataCategory in data:
            individual_words[dataCategory.categoryName] =  self.getWordsFromIndividual(dataCategory)

        self.score = TFIDF.compute(individual_words)
        Model_Goodness.compute(individual_words, data, self)

    def getWordsFromIndividual(self, dataCategory: DataCategory):
        indexs = (self.chromosome[dataCategory.categoryName].getSelectedFeatures())
        return dataCategory.getWorsdAt(indexs)

    @staticmethod
    def generateRandom(individual_lenght: int = 0, category_lenghts: dict = {}) -> Individual:
        individual = Individual(category_lenghts=category_lenghts)

        for category in category_lenghts:
            threshold = Individual.MAX_INDIVIDUAL_FEATURES / category_lenghts[category]

            for index in range(category_lenghts[category]):
                if (random.uniform(0, 1) < threshold):
                    individual.chromosome[category].alterGen(index)

        return individual

    def __str__(self):
        return str(self.chromosome)

    def __repr__(self):
        return str(self.chromosome)

    @staticmethod
    def setMaxIndividualFeatures(maxIndividualFeatures: int) -> None:
        Individual.MAX_INDIVIDUAL_FEATURES = maxIndividualFeatures