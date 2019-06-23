from Log import *
from Genetic.Individual import *


class BaseCrossover:

    @classmethod
    def crossover(cls, individual_1: BaseIndividual, individual_2: BaseIndividual, individual_type: BaseIndividual,
                  crossover_prob: float):
        LoggerHandler.error(cls.__name__, f"You must add a crossover() definition for '{cls.__name__}'.")