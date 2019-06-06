from EmailParser import DataCategory
from Log import LoggerHandler
from Genetic.Components import Population, Individual, Chromosome
from Genetic.Fitness import TFIDF, Model_Goodness
from Genetic.Simple_GA_Specification import SimpleGASpecification
from Genetic.SelectionMethods import SelectionMethods, Roulette_Wheel
from Genetic.ReplacementMethods import ReplacementMethods, SelectiveReplacement
from Genetic.Operations import Mutation, Crossover
from Utilities import FileUtilities
import matplotlib.pyplot as plt
import itertools


class Simple_GA():

    MAX_GENERATIONS: int
    GRAPHIC: bool
    IMPROVE: bool

    def __init__(self, problem_specification: SimpleGASpecification, generations: int, graphic: bool, improve: bool):
        self.train_data: list[DataCategory] = problem_specification.train_data
        self.test_data: list[DataCategory] = problem_specification.test_data
        self.population: list[Individual] = problem_specification.population

        Simple_GA.MAX_GENERATIONS = generations
        Simple_GA.GRAPHIC = graphic
        Simple_GA.IMPROVE = improve
        SelectionMethods.Roulette_Wheel = Roulette_Wheel
        ReplacementMethods.SelectiveReplacement = SelectiveReplacement
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def startUpGA(self) -> None:
        for train_data_category in self.train_data:
            TFIDF.calculateTFIDF(train_data_category)

        for individual in self.population:
            individual.calculateScore(self.train_data)

        LoggerHandler.log(__name__, "Fitness calculated for initial population!")

        actual_generation = 0

        if Simple_GA.GRAPHIC:
            plt.axis([0, Simple_GA.MAX_GENERATIONS, 0, 1])

        while actual_generation < Simple_GA.MAX_GENERATIONS:
            parent_1 = SelectionMethods.Roulette_Wheel.getParents(self.population)
            parent_2 = SelectionMethods.Roulette_Wheel.getParents(self.population)
            self.population.append(parent_1)
            self.population.append(parent_2)

            offspring_1, offspring_2 = Crossover.apply(parent_1, parent_2)
            offspring_1.calculateScore(self.train_data)
            offspring_2.calculateScore(self.train_data)

            if offspring_1.score > offspring_2.score:
                best_offspring = offspring_1
            else:
                best_offspring = offspring_2

            best_offspring = Mutation.apply(best_offspring)
            best_offspring.calculateScore(self.train_data)

            ReplacementMethods.SelectiveReplacement.replacement(parent_1, parent_2, best_offspring, self.population, self.train_data)

            if Simple_GA.GRAPHIC:
                self.population.sort(key=lambda individual: individual.score, reverse=True)
                colors = itertools.cycle(["r"])
                print(self.population[0].score)
                plt.scatter(actual_generation, self.population[0].score, color=next(colors))
                plt.pause(0.05)

            LoggerHandler.log(__name__, f"Generation {actual_generation}")
            actual_generation += 1
