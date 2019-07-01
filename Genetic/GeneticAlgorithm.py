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
import time


class GeneticAlgorithm:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification, TEST_DIR: str, execution_id: int):
        self.problemSpecification: GeneticAlgorithmSpecification = problemSpecification
        self.config: dict = problemSpecification.config
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

        # TEST_INFORMATION
        self.BEST_INDIVIDUAL = None
        self.TEST_DIR = TEST_DIR
        self.EXECUTION_ID = execution_id
        self.RESULTS: dict = {"results": []}

    def start(self, start_time, graphic_mode: bool = False) -> tuple:

        for individual in self.population:
            Classifier.evaluate(individual, self.problemSpecification.train_data, 1.0)
            PenaltyDistribution.penalize(individual)

        self.population = sorted(self.population, reverse=True)
        LoggerHandler.log(__name__,
                          f"0th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")

        if graphic_mode:
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
            if graphic_mode:
                plt.scatter(actual_generation, (sum([individual.score for individual in self.population])/len(self.population)))
                plt.pause(0.05)

        if graphic_mode:
            plt.savefig(self.TEST_DIR + '/graph_' + str(self.EXECUTION_ID) + '.png')
            plt.clf()

        self.BEST_INDIVIDUAL = json.dumps(individual, indent=5, cls=BaseIndividualEncoder)
        return (int((time.time() - start_time)), self.RESULTS['results'])

    def get_solution(self) -> dict:
        self.population = sorted(self.population, reverse=True)
        best_solution: BaseIndividual = self.population[0]
        return best_solution.chromosome.chromosome_distribution()

    def __save_generation__(self, generation: int):
        chromosome_distribution: list = []

        for individual in self.population:
            chromosome_distribution.append(list(individual.chromosome.__compute_distribution__().values()))

        chromosome_distribution = np.sum(chromosome_distribution, axis=0) / len(chromosome_distribution)
        chromosome_distribution = list(np.true_divide(chromosome_distribution, len(BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION)))

        generation_info: dict = {
            "generation_" + str(generation): {
                "average_score": sum([individual.score for individual in self.population]) / len(self.population),
                "average_individual_size": sum([len(individual.chromosome.selected_gens) for individual in self.population]) / len(self.population),
                "average_distribution": chromosome_distribution,
                "best_individual_score": self.population[0].score,
                "best_individual_distribution": self.population[0].chromosome.__compute_distribution__(),
                "best_individual_size": self.population[0].chromosome.selected_gens_size
            }
        }

        self.RESULTS['results'].append(generation_info)