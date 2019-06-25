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
                 population_updater: str, population_generator: str, max_generations: int,
                 parent_selector: str, population_size: int, penalty: float):

        self.config: dict = {
            "chromosome": BaseChromosome.type["BaseChromosome"],
            "gen": BaseGen.type["BaseGen"],
            "individual": BaseIndividual.type["BaseIndividual"],
            "population_updater": PopulationUpdaters.type[population_updater],
            "parent_selector": ParentSelector.type[parent_selector],
            "penalization_function": PenaltyFunctions.type["PenaltyDistribution"],
            "crossover": CrossoverTypes.type["UniformCrossover"],
            "mutation": BaseMutation.type["ControlledMutation"],
        }

        self.config["penalization_function"].RATE = penalty
        self.config["crossover"].RATE = penalty
        self.config["mutation"].RATE = mutation_prob
        self.train_data: [DataCategory] = train_data
        self.max_generations: int = max_generations

        shuffle_train_data: [DataCategory] = self.__shuffle_train_data__(copy.deepcopy(train_data))
        self.population: [BaseIndividual] = PopulationGenerator.type[population_generator].generate(
            generator_type=population_generator,
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