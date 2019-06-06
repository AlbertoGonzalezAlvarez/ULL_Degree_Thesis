from EmailParser import DataCategory
from Log.LoggerHandler import LoggerHandler
from Genetic.Fitness import TFIDF
from Genetic.Operations import Mutation, Crossover
from Genetic.Components import Population, Individual

class SimpleGASpecification:

    def __init__(self, train_data: DataCategory, test_data: DataCategory, mutation_rate: float = 0.1,
                 populationSize: int = 0, maxIndividualFeatures: int = 0, fitness_penalization: float = 0.0,
                 cutting_points: int = 0, gt_max_features: float = 0.0):

        Population.setMaxPopulationSize(populationSize)
        Individual.setMaxIndividualFeatures(maxIndividualFeatures)
        TFIDF.PENALIZATION_BAD_CATEGORY = fitness_penalization
        TFIDF.PENALIZATION_GT_MAX_FEATURES = gt_max_features
        Mutation.MUTATION_RATE = mutation_rate
        Crossover.CUTTING_POINTS = cutting_points

        self.train_data: list[DataCategory] = train_data
        self.test_data: list[DataCategory] = test_data
        self.population: list[Individual] = []

        category_lenghts = {}
        for category_data in train_data:
            category_lenghts[category_data.name] = category_data.lenght - 1

        for _ in range(Population.MAX_POPULATION_SIZE):
            individual: Individual = Individual.generateRandom(category_lenghts=category_lenghts)
            self.population.append(individual)

