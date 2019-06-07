from Log import LoggerHandler
from Genetic.Components import Individual


class Fitness:
    PENALIZATION = 0.001

    @classmethod
    def compute(cls):
        LoggerHandler.error(cls.__name__, f"You must add a compute() definition for '{cls.__name__}'.")
