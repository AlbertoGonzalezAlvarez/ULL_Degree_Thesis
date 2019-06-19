from EmailParser import DataCategory
from Log import LoggerHandler
from Genetic.Components import Population, Individual, Chromosome
from Genetic.Fitness import TFIDF, Model_Goodness
from Genetic.Simple_GA_Specification import SimpleGASpecification
from Genetic.SelectionMethods import SelectionMethods, Roulette_Wheel, RandomSelection, TournamentSelection
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
        SelectionMethods.RandomSelection = RandomSelection
        ReplacementMethods.SelectiveReplacement = SelectiveReplacement
        SelectionMethods.TournamentSelection = TournamentSelection
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

        next_population: list[Individual] = []
        original_population: list[Individual] = []

        while actual_generation < Simple_GA.MAX_GENERATIONS:
            original_population = self.population[:]
            while len(self.population) != 0:
                parent_1 = SelectionMethods.Roulette_Wheel.getParents(self.population)
                parent_2 = SelectionMethods.Roulette_Wheel.getParents(self.population)

                offspring_1, offspring_2 = Crossover.apply(parent_1, parent_2)
                # offspring_1 = Mutation.apply(offspring_1)
                # offspring_2 = Mutation.apply(offspring_2)

                offspring_1.calculateScore(self.train_data)
                offspring_2.calculateScore(self.train_data)

                if parent_1.score >= parent_2.score:
                    best_parent = parent_1
                    worst_parent = parent_2
                else:
                    best_parent = parent_2
                    worst_parent = parent_1

                if offspring_1.score > offspring_2.score:
                    best_offspring = offspring_1
                    worst_offspring = offspring_2
                else:
                    best_offspring = offspring_2
                    worst_offspring = offspring_1


                if best_offspring.score > worst_parent.score:
                    next_population.append(best_offspring)

                    if worst_offspring.score > best_parent.score:
                        next_population.append(worst_offspring)
                    else:
                        next_population.append(best_parent)
                else:
                    next_population.append(parent_1)
                    next_population.append(parent_2)

            next_population.sort(key=lambda individual: individual.score, reverse=True)
            LoggerHandler.log(__name__, f"Best individual => [{next_population[0].score}: {len(next_population[0])}]")
            LoggerHandler.log(__name__, f"Generation {actual_generation}")
            del self.population
            self.population = next_population[:]
            next_population.clear()
            actual_generation += 1
