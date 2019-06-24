from Genetic import *
from Log import LoggerHandler
import copy


class GeneticAlgorithm:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification):
        self.config: GeneticAlgorithmSpecification = problemSpecification
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def start(self):
        actual_generation: int = 0

        parent_1: BaseIndividual = self.config.parent_selector.select_parent(self.population)
        parent_2: BaseIndividual = self.config.parent_selector.select_parent(self.population)