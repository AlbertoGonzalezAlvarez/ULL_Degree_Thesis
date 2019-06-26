from Genetic.Gen import *
from Genetic.Individual import *
from Genetic.ParentSelector import *
import random

class AgeFitness(ParentSelector):

    COEFFICIENT: int = 20

    @staticmethod
    def select_parent(population: [BaseIndividual]):

        for index in range(len(population)):
            if population[index].age < AgeFitness.COEFFICIENT:
                selected_individual = population.pop(index)
                selected_individual.incrementAge()
                return selected_individual


