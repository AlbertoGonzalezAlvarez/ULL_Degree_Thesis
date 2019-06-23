from Genetic.Gen import *
from Log.LoggerHandler import *

class ParentSelector:
    type = {}

    def __init_subclass__(cls):
        ParentSelector.type.update({cls.__name__: cls})

    @classmethod
    def select_parent(cls, population: [BaseGen]):
        LoggerHandler.error(cls.__name__, f"You must add a select_parent() function to '{cls.__name__}'.")