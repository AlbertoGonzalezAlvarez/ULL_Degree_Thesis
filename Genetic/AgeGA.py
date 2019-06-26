from Genetic import *
from Log import LoggerHandler
import copy


class AgeGA:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification):
        self.problemSpecification: GeneticAlgorithmSpecification = problemSpecification
        self.config: dict = problemSpecification.config
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def start(self):

        for individual in self.population:
            TFIDF.evaluate(individual, self.problemSpecification.train_data, 0.2)
            Classifier.evaluate(individual, self.problemSpecification.train_data, 0.8)
            PenaltyDistribution.penalize(individual)

        self.population = sorted(self.population, reverse=True)
        LoggerHandler.log(__name__,
                          f"0th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")

        for actual_generation in range(self.problemSpecification.max_generations):
            parent_1: BaseIndividual = self.config["parent_selector"].select_parent(self.population)
            parent_2: BaseIndividual = self.config["parent_selector"].select_parent(self.population)

            for individual in self.population:
                individual.resetAge()

            self.population.append(parent_2)
            self.population.append(parent_1)

            offspring_1: BaseIndividual = UniformCrossover.crossover(parent_1, parent_2, self.config['individual'],
                                                                         self.config['chromosome'])

            ControlledMutation.mutate(offspring_1)

            TFIDF.evaluate(offspring_1, self.problemSpecification.train_data, 0.2)
            Classifier.evaluate(offspring_1, self.problemSpecification.train_data, 0.8)
            PenaltyDistribution.penalize(offspring_1)

            self.population = sorted(ReplaceWorst.replace(self.population, parent_1, parent_2, offspring_1, offspring_1), reverse=True)
            LoggerHandler.log(__name__, f"{actual_generation}th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")
