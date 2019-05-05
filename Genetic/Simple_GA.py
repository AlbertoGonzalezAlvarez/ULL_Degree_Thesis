from Genetic.Operations.Mutation import Mutation
from Log.LoggerHandler import LoggerHandler
from Genetic.Chromosome import Chromosome
from Genetic.Fitness import Fitness
import random

class Simple_GA():

    def __init__(self, train_data, test_data: dict, mutation_rate: float = 0.1, initialPopulationSize: int = 0):
        self.train_data = train_data
        self.test_data = test_data
        self.initialPopulationSize = initialPopulationSize
        self.population = {}
        self.individuals_lenght = {}
        self.fitnesFunc = Fitness.startUp(self)

        if mutation_rate > 0.0 and mutation_rate <= 1.0:
            Mutation.MUTATION_RATE = mutation_rate
        else:
            LoggerHandler.error(__name__, "Mutation rate should be between (0.0 - 1.0]")

        for category in train_data:
            self.population[category] = []

        Fitness

    def generateInitialSolution(self, selectedFeatures: int):
        # Calculate TF-IDF score


        # Initialize population
        for category in self.population:
            self.individuals_lenght[category] = sum(email.contentLenght for email in self.train_data[category])
            for i in range(self.initialPopulationSize):
                individual = Chromosome(self.individuals_lenght[category])
                self.population[category].append(individual)

        LoggerHandler.log(__name__, "Population has been initialized.")

        # Generate random genes for each individual
        for category in self.population:
            for index in range(self.initialPopulationSize):
                threshold = selectedFeatures/self.individuals_lenght[category]
                for gen in self.population[category][index]:
                    if (random.uniform(0, 1) < threshold):
                        gen.selectGen()

        LoggerHandler.log(__name__, "Initial population genes haven changed randomly.")
        LoggerHandler.log(__name__, "Ready to start!")

        # Fitness.computeFitness(self)
    def startUpGA(self):
        pass


