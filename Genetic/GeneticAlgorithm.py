from Genetic import *
from Log import LoggerHandler
import copy
import matplotlib.pyplot as plt
import itertools
import random
import Utilities


class GeneticAlgorithm:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification):
        self.problemSpecification: GeneticAlgorithmSpecification = problemSpecification
        self.config: dict = problemSpecification.config
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def start(self):
        plt.axis([0, self.problemSpecification.max_generations, -1, 1])
        for individual in self.population:
            # TFIDF.evaluate(individual, self.problemSpecification.train_data, 1)
            Classifier.evaluate(individual, self.problemSpecification.train_data, 1.0)
            PenaltyDistribution.penalize(individual)

        self.population = sorted(self.population, reverse=True)
        LoggerHandler.log(__name__,
                          f"0th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")

        plt.scatter(0, (sum([individual.score for individual in self.population]) / len(self.population)))
        plt.pause(0.05)

        # dic = {"generation_0": self.population,
        #        "average_punctuation": (sum([individual.score for individual in self.population])/len(self.population))}
        # Utilities.FileUtilities.writeToFile(dic, "result.json", encoder = BaseIndividualEncoder)

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

                    # TFIDF.evaluate(offspring_1, self.problemSpecification.train_data, 0.2)
                    Classifier.evaluate(offspring_1, self.problemSpecification.train_data, 1.0)
                    # TFIDF.evaluate(offspring_2, self.problemSpecification.train_data, 0.2)
                    Classifier.evaluate(offspring_2, self.problemSpecification.train_data, 1.0)

                    PenaltyDistribution.penalize(offspring_1)
                    PenaltyDistribution.penalize(offspring_2)

                    next_population.append(offspring_1)
                    next_population.append(offspring_2)
                else:
                    next_population.append(parent_2)
                    next_population.append(parent_1)


            self.population = self.config["population_updater"].update(actual_population, next_population)
            LoggerHandler.log(__name__, f"{actual_generation}th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")
            LoggerHandler.log(__name__,
                              f"{actual_generation}th generation: Average individual size => [{sum([len(individual.chromosome.selected_gens) for individual in self.population])/len(self.population)}]")
            if True:
                plt.scatter(actual_generation, (sum([individual.score for individual in self.population])/len(self.population)))
                plt.pause(0.05)

            next_population.clear()

        dic = {"last_generation": self.population,
               "average_punctuation": (
                           sum([individual.score for individual in self.population]) / len(self.population)),
               "average_size":  sum([len(individual.chromosome.selected_gens) for individual in self.population]) / len(self.population)}
        Utilities.FileUtilities.writeToFile(dic, "result.json", encoder=BaseIndividualEncoder)