from Genetic.Operations.Mutation import Mutation
from EmailParser.DataCategory import DataCategory
from Log.LoggerHandler import LoggerHandler
from Genetic.Population import Population
from Genetic.Chromosome import Chromosome
from Genetic.Fitness import Fitness
from Genetic.Individual import Individual
from Genetic.GAData import GAData
import random

class Simple_GA():

    def __init__(self, problem_specification: GAData) -> None:
        self.train_data: list[DataCategory] = problem_specification.train_data
        self.test_data: list[DataCategory] = problem_specification.test_data
        self.population: list[Population] = problem_specification.population

        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def startUpGA(self) -> None:
        # print(self.test_data[0].corpus[0])
        # for population_index in range(len(self.population)):
            # population.calculateIndividualsScore()
        self.population[0].calculateIndividualsScore(self.test_data[0])
