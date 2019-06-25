from Log import *
from Genetic.Individual import *


class BaseMutation:

    type = {}
    RATE: float = 0.0

    def __init_subclass__(cls):
        BaseMutation.type.update({cls.__name__: cls})

    @classmethod
    def mutate(cls, individual: BaseIndividual):
        LoggerHandler.error(cls.__name__, f"You must add a mutation() definition for '{cls.__name__}'.")