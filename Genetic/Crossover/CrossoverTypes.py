from Log import *
from Genetic.Individual import *


class CrossoverTypes:

    type = {}
    RATE: float = 0.0

    def __init_subclass__(cls):
        CrossoverTypes.type.update({cls.__name__: cls})

    @classmethod
    def crossover(cls, individual_1: BaseIndividual, individual_2: BaseIndividual, individual_type: BaseIndividual):
        LoggerHandler.error(cls.__name__, f"You must add a crossover() definition for '{cls.__name__}'.")