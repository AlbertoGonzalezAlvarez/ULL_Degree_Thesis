from EmailParser.DataCategories import DataCategories
from Log.LoggerHandler import LoggerHandler
from Genetic.Population import Population
from Genetic.Individual import Individual


class GAData:

    def __init__(self, train_data: DataCategories, test_data: DataCategories, mutation_rate: float = 0.1,
                 populationSize: int = 0, maxIndividualFeatures: int = 0) -> None:

        Population.setMaxPopulationSize(populationSize)
        Individual.setMaxIndividualFeatures(maxIndividualFeatures)

        self.train_data: DataCategories = train_data
        self.test_data: DataCategories = test_data
        self.population: Population = []

        for category in train_data:
            self.population.append(Population(category.lenght))
            LoggerHandler.log(__name__, f"Population for category '{category.name}' has been initialized.")

        LoggerHandler.log(__name__, "Ready to start!")

