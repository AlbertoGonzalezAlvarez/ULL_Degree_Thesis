from Log import LoggerHandler
from Genetic.Components import Individual


class Fitness:

    PENALIZATION_BAD_CATEGORY = 0.0
    PENALIZATION_GT_MAX_FEATURES = 0.0

    @classmethod
    def compute(cls):
        LoggerHandler.error(cls.__name__, f"You must add a compute() definition for '{cls.__name__}'.")
