from Genetic import *
from Log import LoggerHandler
import copy


class GeneticAlgorithm:

    def __init__(self, problemSpecification: GeneticAlgorithmSpecification):
        self.problemSpecification: GeneticAlgorithmSpecification = problemSpecification
        self.config: dict = problemSpecification.config
        self.population: [BaseGen] = problemSpecification.population
        LoggerHandler.log(__name__, "Problem specification loaded, ready to start!")

    def start(self):
        actual_generation: int = 0

        for individual in self.population:
            TFIDF.evaluate(individual, self.problemSpecification.train_data, 0.2)
            Classifier.evaluate(individual, self.problemSpecification.train_data, 0.8)
            PenaltyDistribution.penalize(individual, self.problemSpecification.penalty)


        parent_1: BaseIndividual = self.config["parent_selector"].select_parent(self.population)
        parent_2: BaseIndividual = self.config["parent_selector"].select_parent(self.population)

        offspring_1: BaseIndividual = UniformCrossover.crossover(parent_1, parent_2, self.config['individual'],
                                                                 self.config['chromosome'], self.problemSpecification.crossover_prob)
        offspring_2: BaseIndividual = UniformCrossover.crossover(parent_1, parent_2, self.config['individual'],
                                                                 self.config['chromosome'], self.problemSpecification.crossover_prob)

        ControlledMutation.mutate(offspring_1, self.problemSpecification.mutation_prob)
        ControlledMutation.mutate(offspring_2, self.problemSpecification.mutation_prob)

        TFIDF.evaluate(offspring_1, self.problemSpecification.train_data, 0.2)
        Classifier.evaluate(offspring_1, self.problemSpecification.train_data, 0.8)
        TFIDF.evaluate(offspring_2, self.problemSpecification.train_data, 0.2)
        Classifier.evaluate(offspring_2, self.problemSpecification.train_data, 0.8)

        next_population = [offspring_1, offspring_2]
        self.config["population_updater"].update(self.population, next_population)

        # PenaltyDistribution.penalize(offspring_1, self.problemSpecification.penalty)
        # SelectiveReplacement.replace(self.population, parent_1, parent_2, offspring_1, offspring_2)
