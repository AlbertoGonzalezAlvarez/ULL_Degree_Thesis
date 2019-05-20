from EmailParser.DataCategory import DataCategory
from Log.LoggerHandler import LoggerHandler
from Genetic.Population import Population
from Genetic.Individual import Individual


class GAData:

    def __init__(self, train_data: DataCategory, test_data: DataCategory, mutation_rate: float = 0.1,
                 populationSize: int = 0, maxIndividualFeatures: int = 0) -> None:

        Population.setMaxPopulationSize(populationSize)
        Individual.setMaxIndividualFeatures(maxIndividualFeatures)

        self.train_data: list[DataCategory] = train_data
        self.test_data: list[DataCategory] = test_data
        self.population: list[Population] = []

        for category_data in train_data:
            self.population.append(Population(category_data.corpus))
            LoggerHandler.log(__name__, f"Population for category_data '{category_data.name}' has been initialized.")
