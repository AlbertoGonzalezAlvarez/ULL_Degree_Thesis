from __future__ import annotations
from Genetic.Individual import Individual
from Log.LoggerHandler import LoggerHandler

class Population():
    MAX_POPULATION_SIZE = 0

    def __init__(self, lenght: int = 0) -> None:
        self.lenght: int = lenght
        self.individuals: list = []

        for _ in range(Population.MAX_POPULATION_SIZE):
            individual: Individual = Individual.generateRandom(individual_lenght=lenght)
            if individual.chromosome.getSelectedFeaturesSize() > 0:
                self.individuals.append(individual)


    def __repr__(self):
        return str(self.individuals)

    def __str__(self):
        return str(self.individuals)

    @staticmethod
    def setMaxPopulationSize(maxPopulationSize: int):
        Population.MAX_POPULATION_SIZE = maxPopulationSize