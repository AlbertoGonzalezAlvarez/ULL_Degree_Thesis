from EmailParser import DataCategory
from Log import LoggerHandler
from Genetic.Components import Population
from Genetic.Fitness import Fitness
from Genetic.Simple_GA_Specification import SimpleGASpecification
from Genetic.SelectionMethods import SelectionMethods, Roulette_Wheel
from Genetic.ReplacementMethods import ReplacementMethods, SelectiveReplacement
from Genetic.Operations import Mutation, Crossover


class Simple_GA():

    def __init__(self, problem_specification: SimpleGASpecification):
        SelectionMethods.Roulette_Wheel = Roulette_Wheel
        ReplacementMethods.SelectiveReplacement = SelectiveReplacement

        self.train_data: list[DataCategory] = problem_specification.train_data
        self.test_data: list[DataCategory] = problem_specification.test_data
        self.population: list[Population] = problem_specification.population

        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def startUpGA(self) -> None:
        for train_data_category in self.train_data:
            Fitness.calculateTFIDF(train_data_category)

        for population in self.population:
            population.calculateIndividualsScore(population.individuals, self.train_data[self.population.index(population)])

        LoggerHandler.log(__name__, "Fitness calculated for initial population!")

        parent_1 = SelectionMethods.Roulette_Wheel.getParents(self.population[0])
        parent_2 = SelectionMethods.Roulette_Wheel.getParents(self.population[0])
        print(parent_1)
        print(parent_2)

        offspring_1, offspring_2 = Crossover.apply(parent_1, parent_2)
        offspring_1 = Mutation.apply(offspring_1)
        offspring_2 = Mutation.apply(offspring_2)

        Population.calculateIndividualsScore(offspring_1, self.train_data[0])
        Population.calculateIndividualsScore(offspring_2, self.train_data[0])
        # print(parent_1)
        # print(parent_2)
        print(offspring_1)
        print(self.population[0])
        print(".----------.")
        ReplacementMethods.SelectiveReplacement.calculateNextPopulation(parent_1, parent_2, offspring_1, self.population[0])
        print(self.population[0])
