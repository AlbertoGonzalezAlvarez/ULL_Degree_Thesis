from Genetic import *
from Log import LoggerHandler
import copy


class GeneticAlgorithm:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification):
        self.problemSpecification: GeneticAlgorithmSpecification = problemSpecification
        self.config: dict = problemSpecification.config
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def start(self):
        actual_generation: int = 0

        # parent_1: BaseIndividual = self.problemSpecification.parent_selector.select_parent(self.population)
        # parent_2: BaseIndividual = self.problemSpecification.parent_selector.select_parent(self.population)
        #
        # offspring_1: BaseIndividual = UniformCrossover.crossover(parent_1, parent_2, self.config['individual'], self.problemSpecification.crossover_prob)
        # print("asd")