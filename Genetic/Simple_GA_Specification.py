from EmailParser import DataCategory
from Log.LoggerHandler import LoggerHandler
from Genetic.Fitness import Fitness
from Genetic.Operations import Mutation, Crossover
from Genetic.Components import Population, Individual

class SimpleGASpecification:
    category_lenghts = {}

    def __init__(self, train_data: DataCategory, test_data: DataCategory, mutation_rate: float = 0.1,
                 populationSize: int = 0, maxIndividualFeatures: int = 0, fitness_penalization: float = 0.0, cutting_points: int = 0):

        category_max_indv_size = {}
        for category_data in train_data:
            category_max_indv_size[category_data.name] = int(maxIndividualFeatures * category_data.lenght) - 1

        Population.setMaxPopulationSize(populationSize)
        Individual.setMaxIndividualFeatures(category_max_indv_size)
        Fitness.PENALIZATION = fitness_penalization
        Mutation.MUTATION_RATE = mutation_rate
        Crossover.CUTTING_POINTS = cutting_points

        self.train_data: list[DataCategory] = train_data
        self.test_data: list[DataCategory] = test_data
        self.population: list[Individual] = []

        for category_data in train_data:
            SimpleGASpecification.category_lenghts[category_data.name] = category_data.lenght - 1

        # print(category_lenghts)
        for _ in range(Population.MAX_POPULATION_SIZE):

            individual: Individual = Individual.generateRandom(category_lenghts=SimpleGASpecification.category_lenghts)
            self.population.append(individual)

