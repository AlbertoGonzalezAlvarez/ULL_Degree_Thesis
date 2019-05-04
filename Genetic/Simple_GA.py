from Genetic.Operations.Mutation import Mutation
from Log.LoggerHandler import LoggerHandler

class Simple_GA:

    def __init__(self, train_data, test_data: dict, mutation_rate: float = 0.1, initialPopulationSize: int = 0):
        self.train_data = train_data
        self.test_data = test_data
        self.initialPopulationSize = initialPopulationSize
        self.population = {}

        if mutation_rate > 0.0 and mutation_rate <= 1.0:
            Mutation.MUTATION_RATE = mutation_rate
        else:
            LoggerHandler.error(__name__, "Mutation rate should be between (0.0 - 1.0]")

        for category in train_data:
            self.population[category] = []

    def startUpGA(self):
        for category in self.population:
            for i in range(self.initialPopulationSize):
                pass



