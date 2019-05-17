from Genetic.Operations.Mutation import Mutation
from Log.LoggerHandler import LoggerHandler
from Genetic.Population import Population
from Genetic.Chromosome import Chromosome
from Genetic.Fitness import Fitness
from Genetic.Individual import Individual
import random

class Simple_GA():

    def __init__(self, train_data, test_data: type, mutation_rate: float = 0.1,
                 populationSize: int = 0, maxIndividualFeatures: int = 0):

        Population.SIZE = populationSize
        Individual.MAX_INDIVIDUAL_FEATURES = maxIndividualFeatures

        self.train_data = train_data
        self.test_data = test_data
        self.population = [Population(category.lenght, ) for category in train_data]

        # self.individuals_lenght = {}
        #
        # #temporal
        # self.train_joined_words = self.joinWords(train_data)
        # # print(self.train_joined_words['soc.religion.christian'][0])
        # self.test_data_joined = []
        #
        # for category in test_data:
        #     for email in test_data[category]:
        #         self.test_data_joined.append(email.content)
        #
        # self.test_data_labels = []
        # i = 0
        # for category in test_data:
        #     for _ in range(len(test_data[category])):
        #         self.test_data_labels.append(i)
        #     i = i + 1
        #
        #
        # # print(len(self.test_data_joined))
        # if mutation_rate > 0.0 and mutation_rate <= 1.0:
        #     Mutation.MUTATION_RATE = mutation_rate
        # else:
        #     LoggerHandler.error(__name__, "Mutation rate should be between (0.0 - 1.0]")
        #
        # for category in train_data:
        #     self.population[category] = []

    def generateInitialSolution(self, selectedFeatures: int):
        # Initialize population
        for category in self.population:
            self.individuals_lenght[category] = sum(email.contentLenght for email in self.train_data[category])
            for _ in range(self.initialPopulationSize):
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
                        gen.updateWord(self.train_joined_words[category][self.population[category][index].getSelectedFeatures()[-1]])

        LoggerHandler.log(__name__, "Initial population genes haven changed randomly.")
        LoggerHandler.log(__name__, "Ready to start!")

        # Calculate score
        print(Fitness.compute(self.population, self.test_data_joined, self.test_data_labels))

    def startUpGA(self):
        pass

    def joinWords(self, data):
        joined_data = {}

        for category in data:
            joined_data[category] = []
            for email in data[category]:
                joined_data[category] = joined_data[category] + email.words

        return joined_data