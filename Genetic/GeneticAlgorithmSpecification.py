from Genetic.PopulationUpdaters import *
from Genetic.PopulationGenerators import *
from Genetic.Individual import *
from Genetic.ParentSelector import *
from Genetic.PenaltyFunctions import *
from Genetic.Chromosome import *
from Genetic.Gen import *
from Genetic.Crossover import *
from Genetic.Mutation import *
from EmailParser.DataCategory import *
import copy
import random

class GeneticAlgorithmSpecification:
    def __init__(self, crossover_prob: float, mutation_prob: float, train_data: [DataCategory], individual_max_len: int,
                    max_generations: int, population_size: int, penalty: float, **config):

        self.config: dict = {
            "chromosome": BaseChromosome.type[config["chromosome"]],
            "gen": BaseGen.type[config["gen"]],
            "individual": BaseIndividual.type[config["individual"]],
            "population_updater": PopulationUpdaters.type[config["population_updater"]],
            "parent_selector": ParentSelector.type[config["parent_selector"]],
            "penalization_function": PenaltyFunctions.type[config["penalization_function"]],
            "crossover": CrossoverTypes.type[config["crossover"]],
            "mutation": BaseMutation.type[config["mutation"]],
            "population_generator": PopulationGenerator.type[config["population_generator"]]
        }

        PenaltyFunctions.RATE = penalty
        CrossoverTypes.RATE = crossover_prob
        BaseMutation.RATE = mutation_prob

        self.train_data: [DataCategory] = train_data
        self.max_generations: int = max_generations

        shuffle_train_data: [DataCategory] = self.__shuffle_train_data__(copy.deepcopy(train_data))
        self.population: [BaseIndividual] =self.config["population_generator"].generate(
            generator_type=self.config["population_generator"],
            chromosome_type=self.config["chromosome"],
            gen_type=self.config["gen"],
            individual_type=self.config["individual"],
            population_size=population_size,
            train_data=shuffle_train_data,
            percentage_of_features=individual_max_len
        )

        LoggerHandler.log(__name__, f"Problem specification loaded!")

    def __shuffle_train_data__(self, train_data: [DataCategory]):
        for category in train_data:
            random.shuffle(category.corpus)

        return train_data