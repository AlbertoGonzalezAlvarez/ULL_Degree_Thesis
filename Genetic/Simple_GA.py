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

    def __init__(self, problem_specification: GAData):

        self.train_data: list[DataCategory] = problem_specification.train_data
        self.test_data: list[DataCategory] = problem_specification.test_data
        self.population: list[Population] = problem_specification.population

        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def startUpGA(self) -> None:
        for train_data_category in self.train_data:
            Fitness.calculateTFIDF(train_data_category)

        for population in self.population:
            population.calculateIndividualsScore(self.train_data[self.population.index(population)])
        LoggerHandler.log(__name__, "Fitness calculated for initial population!")

        for individual in self.population[0].individuals:
            print(individual.score)
            print(Population.getWordsFromIndividuals(individual, self.train_data[0].corpus))

