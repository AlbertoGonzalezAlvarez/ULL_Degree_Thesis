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
        SelectionMethods.Roulette_Wheel = Roulette_Wheel
        ReplacementMethods.SelectiveReplacement = SelectiveReplacement

        self.train_data: list[DataCategory] = problem_specification.train_data
        self.test_data: list[DataCategory] = problem_specification.test_data
        self.population: list[Population] = problem_specification.population

        Simple_GA.MAX_GENERATIONS = generations
        Simple_GA.GRAPHIC = graphic
        Simple_GA.IMPROVE = improve

        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def startUpGA(self) -> None:
        for test_data_category in self.test_data:
            TFIDF.calculateTFIDF(test_data_category)

        for population in self.population:
            population.calculateIndividualsScore(population.individuals, self.train_data[self.population.index(population)])

        LoggerHandler.log(__name__, "Fitness calculated for initial population!")

        actual_generation = 0

        if Simple_GA.GRAPHIC:
            plt.axis([0, Simple_GA.MAX_GENERATIONS, 0, 1])

        while actual_generation < Simple_GA.MAX_GENERATIONS:
            if Simple_GA.IMPROVE:
                train_words = {}
                for category_population, index in zip(self.population, range(len(self.population))):
                    train_words[self.train_data[index].categoryName] = \
                        category_population.getWordsFromIndividuals(category_population.individuals, self.train_data[index].corpus)

                # Model_Goodness.compute(train_words, self.test_data, self.population)

            for category_population in self.population:
                population_index = self.population.index(category_population)

                parent_1 = SelectionMethods.Roulette_Wheel.getParents(category_population)
                parent_2 = SelectionMethods.Roulette_Wheel.getParents(category_population)
                category_population.addIndividual(parent_1)
                category_population.addIndividual(parent_2)
                offspring_1, offspring_2 = Crossover.apply(parent_1, parent_2)

                offspring_1 = Mutation.apply(offspring_1)
                offspring_2 = Mutation.apply(offspring_2)
                Population.calculateIndividualsScore(offspring_1, self.train_data[population_index])
                Population.calculateIndividualsScore(offspring_2, self.train_data[population_index])

                ReplacementMethods.SelectiveReplacement.calculateNextPopulation(parent_1, parent_2, offspring_1, category_population)
                ReplacementMethods.SelectiveReplacement.calculateNextPopulation(parent_1, parent_2, offspring_2, category_population)

            if Simple_GA.GRAPHIC:
                colors = itertools.cycle(["r", "b", "g"])
                for category_population, index in zip(self.population, range(len(self.population))):
                    plt.scatter(actual_generation, category_population.getAveragePopulationScore(), label=self.train_data[index].categoryName, color= next(colors))
                    plt.pause(0.05)

                if actual_generation == 0:
                    plt.legend(loc='best', scatterpoints = 1)

            LoggerHandler.log(__name__, f"Generation {actual_generation}")
            actual_generation += 1

        LoggerHandler.log(__name__, "Simple GA has finished!")

        content_to_write = {}
        for category_index in range(len(self.train_data)):
            population = self.population[category_index]
            word_list = Population.getWordsFromIndividuals(population.individuals,
                                                           self.train_data[category_index].corpus)
            joined_category_words = []
            for words in word_list:
                joined_category_words += words
            content_to_write[self.train_data[category_index].categoryName] = joined_category_words
        FileUtilities.writeToFile(content_to_write, "categories_data.json")
