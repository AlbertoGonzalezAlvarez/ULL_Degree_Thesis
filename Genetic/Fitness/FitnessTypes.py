from Genetic.Individual import *
from Log import *
from EmailParser.DataCategory import *


class FitnessTypes:

    type = {}

    def __init_subclass__(cls):
        FitnessTypes.type.update({cls.__name__: cls})

    @classmethod
    def evaluate(cls, individual: BaseIndividual, train_data: [DataCategory], weight: float, multiplier: int = 1):
        LoggerHandler.error(cls.__name__, f"You must add a evaluate() definition for '{cls.__name__}'.")