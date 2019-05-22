from Log import LoggerHandler
from Genetic.Components import Individual


class ReplacementMethods:

    @classmethod
    def calculateNextPopulation(cls, parent_1: Individual, parent_2: Individual, offspring: Individual):
        LoggerHandler.error(cls.__name__, f"You must add a  calculateNextPopulation() definition for '{cls.__name__}'.")
