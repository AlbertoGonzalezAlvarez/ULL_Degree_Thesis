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
    def __init__(self, train_data, **config):

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

        self.params: dict = config
        self.params["crossover_prob"] = config["crossover_prob"]
        self.params["mutation_prob"] = config["mutation_prob"]
        self.params["individual_max_len"] = config["individual_max_len"]
        self.params["max_generations"] = config["max_generations"]
        self.params["population_size"] = config["population_size"]
        self.params["penalty_rate"] = config["penalty_rate"]

        PenaltyFunctions.RATE = config["penalty_rate"]
        CrossoverTypes.RATE = config["crossover_prob"]
        BaseMutation.RATE = config["mutation_prob"]

        self.train_data: [DataCategory] = train_data
        self.max_generations: int = config["max_generations"]

        shuffle_train_data: [DataCategory] = self.__shuffle_train_data__(copy.deepcopy(train_data))
        self.population: [BaseIndividual] =self.config["population_generator"].generate(
            generator_type=self.config["population_generator"],
            chromosome_type=self.config["chromosome"],
            gen_type=self.config["gen"],
            individual_type=self.config["individual"],
            population_size=config["population_size"],
            train_data=shuffle_train_data,
            percentage_of_features=config["individual_max_len"]
        )

        LoggerHandler.log(__name__, f"Problem specification loaded!")

    def __shuffle_train_data__(self, train_data: [DataCategory]):
        for category in train_data:
            random.shuffle(category.corpus)

        return train_data