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

        for individual in self.population:
            TFIDF.evaluate(individual, self.problemSpecification.train_data, 0.2)
            # Classifier.evaluate(individual, self.problemSpecification.train_data, 1)
            PenaltyDistribution.penalize(individual, self.problemSpecification.penalty)

        self.population = sorted(self.population)
        LoggerHandler.log(__name__,
                          f"0th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")

        for actual_generation in range(self.problemSpecification.max_generations):
            next_population = []
            actual_population = self.population[:]
            for _ in range(int(len(self.population)/2)):
                parent_1: BaseIndividual = self.config["parent_selector"].select_parent(self.population)
                parent_2: BaseIndividual = self.config["parent_selector"].select_parent(self.population)

                offspring_1: BaseIndividual = UniformCrossover.crossover(parent_1, parent_2, self.config['individual'],
                                                                         self.config['chromosome'], self.problemSpecification.crossover_prob)
                offspring_2: BaseIndividual = UniformCrossover.crossover(parent_1, parent_2, self.config['individual'],
                                                                         self.config['chromosome'], self.problemSpecification.crossover_prob)

                ControlledMutation.mutate(offspring_1, self.problemSpecification.mutation_prob)
                ControlledMutation.mutate(offspring_2, self.problemSpecification.mutation_prob)

                TFIDF.evaluate(offspring_1, self.problemSpecification.train_data, 0.2)
                # Classifier.evaluate(offspring_1, self.problemSpecification.train_data, 1)
                TFIDF.evaluate(offspring_2, self.problemSpecification.train_data, 0.2)
                # Classifier.evaluate(offspring_2, self.problemSpecification.train_data, 1)

                next_population.append(offspring_1)
                next_population.append(offspring_2)

            self.population = self.config["population_updater"].update(actual_population, next_population)
            LoggerHandler.log(__name__, f"{actual_generation}th generation: Best individual => [{self.population[0].score}: {self.population[0].chromosome.selected_gens_size}]")
            next_population.clear()
