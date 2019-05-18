from Genetic.Operations.Mutation import Mutation
from EmailParser.DataCategories import DataCategories
from Log.LoggerHandler import LoggerHandler
from Genetic.Population import Population
from Genetic.Chromosome import Chromosome
from Genetic.Fitness import Fitness
from Genetic.Individual import Individual
from Genetic.GAData import GAData
import random

class Simple_GA():

    def __init__(self, problem_specification: GAData) -> None:
        self.train_data: DataCategories = problem_specification.train_data
        self.test_data: DataCategories = problem_specification.test_data
        self.population: Population = problem_specification.population

        LoggerHandler.log(__name__, "Problem specification loaded!")

    def startUpGA(self) -> None:
        pass

    # def joinWords(self, data):
    #     joined_data = {}
    #
    #     for category in data:
    #         joined_data[category] = []
    #         for email in data[category]:
    #             joined_data[category] = joined_data[category] + email.words
    #
    #     return joined_data