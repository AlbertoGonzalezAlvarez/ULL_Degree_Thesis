from Genetic.Gen import *
from Genetic.Individual import *
from Genetic.ParentSelector import *
import random

class Tournament(ParentSelector):

    N_CANDIDATES = 2

    @staticmethod
    def select_parent(population: [BaseIndividual]):
        population_copy = population[:]
        random.shuffle(population_copy)

        selected_individuals: list = []

        for _ in range(Tournament.N_CANDIDATES):
            selected_individuals.append(population_copy[random.randint(0, len(population_copy) - 1)])

        selected_individuals.sort(key=lambda individual: individual.score, reverse=True)

        return population.pop(population.index(selected_individuals[0]))