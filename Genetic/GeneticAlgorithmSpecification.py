from Genetic.PopulationUpdaters import *
from Genetic.PopulationGenerators import *
from Genetic.Individual import *
from EmailParser.DataCategory import *

class GeneticAlgorithmSpecification:
    def __init__(self, crossover_prob: float, mutation_prob: float, train_data: [DataCategory], individual_max_len: int,
                 population_updater: PopulationUpdaters, population_generator: PopulationGenerator):

        self.crossover_prob: float = crossover_prob
        self.mutation_prob: float = mutation_prob
        self.train_data: [DataCategory] = train_data
        self.individual_max_len: int = individual_max_len

        self.population_updater: PopulationUpdaters = population_updater

        self.population: [BaseIndividual] = population_generator.generate(train_data)

