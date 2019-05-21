from __future__ import annotations
from Genetic.Individual import Individual
from EmailParser.DataCategory import DataCategory
from Genetic.Fitness import Fitness
from Log.LoggerHandler import LoggerHandler

class Population():
    MAX_POPULATION_SIZE = 0

    def __init__(self, category_data: DataCategory):
        self.corpus_data: DataCategory = category_data
        self.individuals: list[Individual] = []

        for _ in range(Population.MAX_POPULATION_SIZE):
            individual: Individual = Individual.generateRandom(individual_lenght = len(category_data) - 1)
            if individual.chromosome.getSelectedFeaturesSize() > 0:
                self.individuals.append(individual)

    def calculateIndividualsScore(self, corpus_data: DataCategory):
        population_words = Population.getWordsFromIndividuals(self.individuals, corpus_data.corpus)
        Fitness.compute(corpus_data.categoryName, population_words, self.individuals)
        # print("fit")

    @staticmethod
    def getWordsFromIndividuals(individuals, corpus_data: list) -> list[str]:
        population_words = []

        if isinstance(individuals, list):
            for individual in individuals:
                individual_words = []
                for index in individual.chromosome.getSelectedFeatures():
                    individual_words.append(corpus_data[index])

                if len(individual_words) > 0:
                    population_words.append(individual_words)
        else:
            individual_words = []
            for index in individuals.chromosome.getSelectedFeatures():
                individual_words.append(corpus_data[index])

            if len(individual_words) > 0:
                population_words.append(individual_words)

        if len(population_words) > 0:
            return population_words

    def __len__(self):
        return len(self.corpus)

    def __repr__(self):
        return str(self.individuals)

    def __str__(self):
        return str(self.individuals)

    @staticmethod
    def setMaxPopulationSize(maxPopulationSize: int):
        Population.MAX_POPULATION_SIZE = maxPopulationSize
