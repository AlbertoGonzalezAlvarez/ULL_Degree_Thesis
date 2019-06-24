from Genetic.Individual import *
from Genetic.ReplacementMethods import *
from Log import *


class BaseReplacement:

    type = {}

    def __init_subclass__(cls):
        BaseReplacement.type.update({cls.__name__: cls})


    @classmethod
    def replace(cls, population: [BaseIndividual], parent_1: BaseIndividual, parent_2: BaseIndividual, offspring_1: BaseIndividual, offspring_2: BaseIndividual):
        LoggerHandler.error(__name__, f"You must implement replace() method")