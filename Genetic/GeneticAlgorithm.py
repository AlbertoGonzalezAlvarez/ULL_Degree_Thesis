from Genetic import *
from Log import LoggerHandler
import copy
import matplotlib.pyplot as plt
import itertools
import random
import Utilities
import os
import re
import json
import numpy as np

TEST_PREFIX = "test_"
TEST_DIR = "./Data/"
CURRENT_DIR = None
RESULTS:dict = {"results": []}
GRAPHIC: bool = True


class GeneticAlgorithm:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification):
        self.problemSpecification: GeneticAlgorithmSpecification = problemSpecification
        self.config: dict = problemSpecification.config
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")
        self.__register_params__()

    def start(self) -> dict:

        for individual in self.population:
            Classifier.evaluate(individual, self.problemSpecification.train_data, 1.0)
            PenaltyDistribution.penalize(individual)

        self.population = sorted(self.population, reverse=True)
        LoggerHandler.log(__name__,
                          f"0th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")

        if GRAPHIC:
            plt.axis([0, self.problemSpecification.max_generations, 0, 1])
            plt.scatter(0, (sum([individual.score for individual in self.population]) / len(self.population)))
            plt.pause(0.05)

        self.__save_generation__(0)
        for actual_generation in range(1, self.problemSpecification.max_generations):
            next_population = []
            actual_population = self.population[:]
            for _ in range(int(len(self.population)/2)):

                parent_1: BaseIndividual = self.config["parent_selector"].select_parent(self.population)
                parent_2: BaseIndividual = self.config["parent_selector"].select_parent(self.population)

                if random.random() < CrossoverTypes.RATE:
                    offspring_1: BaseIndividual = self.config['crossover'].crossover(parent_1, parent_2, self.config['individual'],
                                                                             self.config['chromosome'])
                    offspring_2: BaseIndividual = self.config['crossover'].crossover(parent_1, parent_2, self.config['individual'],
                                                                             self.config['chromosome'])

                    self.config['mutation'].mutate(offspring_1)
                    self.config['mutation'].mutate(offspring_2)

                    Classifier.evaluate(offspring_1, self.problemSpecification.train_data, 1.0)
                    Classifier.evaluate(offspring_2, self.problemSpecification.train_data, 1.0)

                    self.config['penalization_function'].penalize(offspring_1)
                    self.config['penalization_function'].penalize(offspring_2)

                    next_population.append(offspring_1)
                    next_population.append(offspring_2)
                else:
                    next_population.append(parent_2)
                    next_population.append(parent_1)

            self.population = self.config["population_updater"].update(actual_population, next_population)
            next_population.clear()
            self.__save_generation__(actual_generation)
            LoggerHandler.log(__name__, f"{actual_generation}th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")
            LoggerHandler.log(__name__,
                              f"{actual_generation}th generation: Average individual size => [{sum([len(individual.chromosome.selected_gens) for individual in self.population])/len(self.population)}]")
            if GRAPHIC:
                plt.scatter(actual_generation, (sum([individual.score for individual in self.population])/len(self.population)))
                plt.pause(0.05)

        plt.savefig(CURRENT_DIR + '/graph.png')
        file = open(CURRENT_DIR + "/results.json", "w+")
        file.write(json.dumps(RESULTS, indent=5))
        self.population = sorted(self.population, reverse=True)
        self.__save_individual__(self.population[0])

    def __save_individual__(self, individual: BaseIndividual):
        file = open(CURRENT_DIR + "/best_individual.json", "w+")
        file.write(json.dumps(individual, indent=5, cls=BaseIndividualEncoder))

    def get_solution(self) -> dict:
        self.population = sorted(self.population, reverse=True)
        best_solution: BaseIndividual = self.population[0]
        return best_solution.chromosome.chromosome_distribution()

    def __register_params__(self):
        test_numbers = sorted([int(re.search('\d+', dir).group()) for dir in os.listdir(TEST_DIR) if not '.' in dir])

        if len(test_numbers) != 0:
            next_test_number = test_numbers[-1] + 1
        else:
            next_test_number = 0

        global CURRENT_DIR
        CURRENT_DIR = TEST_DIR + TEST_PREFIX + str(next_test_number)
        os.mkdir(CURRENT_DIR)
        file = open(CURRENT_DIR + "/params.json", "w+")
        file.write(json.dumps(self.problemSpecification.params, indent = 5))

    def __save_generation__(self, generation: int):
        chromosome_distribution: list = []

        for individual in self.population:
            chromosome_distribution.append(list(individual.chromosome.__compute_distribution__().values()))

        chromosome_distribution = np.sum(chromosome_distribution, axis=0)
        chromosome_distribution = list(np.true_divide(chromosome_distribution, len(BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION)))

        generation_info: dict = {
            "generation_" + str(generation): {
                "average_score": sum([individual.score for individual in self.population]) / len(self.population),
                "average_individual_size": sum([len(individual.chromosome.selected_gens) for individual in self.population]) / len(self.population),
                "average_distribution": chromosome_distribution,
                "best_individual_score": self.population[0].score,
                "best_individual_distribution": self.population[0].chromosome.__compute_distribution__()
            }
        }

        RESULTS['results'].append(generation_info)

