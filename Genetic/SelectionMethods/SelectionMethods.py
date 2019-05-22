from Log import LoggerHandler
from Genetic.Components import Population

class SelectionMethods:

    @classmethod
    def getParents(cls, population: Population):
        LoggerHandler.error(cls.__name__, f"You must add a  getParents() definition for '{cls.__name__}'.")