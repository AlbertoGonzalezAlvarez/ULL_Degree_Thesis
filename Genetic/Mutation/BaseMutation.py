from Log import *
from Genetic.Individual import *


class BaseMutation:

    @classmethod
    def mutate(cls, individual: BaseIndividual, mutation_rate: float):
        LoggerHandler.error(cls.__name__, f"You must add a mutation() definition for '{cls.__name__}'.")