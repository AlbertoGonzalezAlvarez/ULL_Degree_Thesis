from __future__ import annotations
from EmailParser import DataCategory
from Genetic.Fitness import Fitness
from Genetic.Components import Individual
from copy import deepcopy


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

    @staticmethod
    def calculateIndividualsScore(individuals: list(Individual), corpus_data: DataCategory):
        if isinstance(individuals, Individual):
            individuals = [individuals]
        population_words = Population.getWordsFromIndividuals(individuals, corpus_data.corpus)
        Fitness.compute(corpus_data.categoryName, population_words, individuals)

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

    def addIndividual(self, individual: Individual):
        self.individuals.append(individual)

    def __len__(self):
        return len(self.individuals)

    def __repr__(self):
        return str(self.individuals)

    def __str__(self):
        return str(self.individuals)

    def pop(self, index: int) -> Individual:
        if index < len(self.individuals):
            return self.individuals.pop(index)

    def getIndividualAt(self, index: int) -> Individual:
        if index < len(self.individuals):
            return self.individuals[index]

    def push(self, individual: Individual):
        self.individuals.append(individual)

    def individualIndex(self, individual: Individual) -> int:
        return self.individuals.index(individual)

    def getNFirstIndividuals(self, start: int = -1, stop: int = -1) -> [Individual]:
        sorted_individuals = sorted(self.individuals, key=lambda individual: individual.score, reverse=True)

        if start != -1 and stop != -1:
            return sorted_individuals[start:stop]
        else:
            return sorted_individuals[start]

    def __copy__(self) -> Population:
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo) -> Population:
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

    @staticmethod
    def setMaxPopulationSize(maxPopulationSize: int):
        Population.MAX_POPULATION_SIZE = maxPopulationSize
