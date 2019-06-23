from Genetic.Individual import BaseIndividual
from Log.LoggerHandler import *

class PenaltyFunctions():
    type = {}

    def __init_subclass__(cls):
        PenaltyFunctions.type.update({cls.__name__: cls})

    @classmethod
    def penalize(cls, individual: BaseIndividual, penalty_rate: float):
        LoggerHandler.error(cls.__name__, f"You must add a penalize() function to '{cls.__name__}'.")