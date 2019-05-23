from EmailParser import DataCategory
from Log import LoggerHandler
from Genetic.Components import Population, Individual, Chromosome
from Genetic.Fitness import Fitness
from Genetic.Simple_GA_Specification import SimpleGASpecification
from Genetic.SelectionMethods import SelectionMethods, Roulette_Wheel
from Genetic.ReplacementMethods import ReplacementMethods, SelectiveReplacement
from Genetic.Operations import Mutation, Crossover
from Utilities import FileUtilities

class Simple_GA():

    def __init__(self, problem_specification: SimpleGASpecification):
        SelectionMethods.Roulette_Wheel = Roulette_Wheel
        ReplacementMethods.SelectiveReplacement = SelectiveReplacement

        self.train_data: list[DataCategory] = problem_specification.train_data
        self.test_data: list[DataCategory] = problem_specification.test_data
        self.population: list[Population] = problem_specification.population

        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def startUpGA(self) -> None:
        for test_data_category in self.test_data:
            Fitness.calculateTFIDF(test_data_category)

        for population in self.population:
            population.calculateIndividualsScore(population.individuals, self.train_data[self.population.index(population)])

        LoggerHandler.log(__name__, "Fitness calculated for initial population!")

        max_generations = 200
        actual_generation = 0

        while actual_generation < max_generations:
            for category_population in self.population:
                population_index = self.population.index(population)

                parent_1 = SelectionMethods.Roulette_Wheel.getParents(category_population)
                parent_2 = SelectionMethods.Roulette_Wheel.getParents(category_population)
                offspring_1, offspring_2 = Crossover.apply(parent_1, parent_2)

                offspring_1 = Mutation.apply(offspring_1)
                offspring_2 = Mutation.apply(offspring_2)
                Population.calculateIndividualsScore(offspring_1, self.train_data[population_index])
                Population.calculateIndividualsScore(offspring_2, self.train_data[population_index])

                ReplacementMethods.SelectiveReplacement.calculateNextPopulation(parent_1, parent_2, offspring_1, category_population)
                actual_generation += 1

        LoggerHandler.log(__name__, "Simple Ga has finished!")

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
