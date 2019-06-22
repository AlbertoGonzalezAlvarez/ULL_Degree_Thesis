from Log import *
from Genetic.Chromosome import *
from Genetic.Gen import *
from Genetic.Individual import *


class PopulationGenerators:

        type = {}

        def __init_subclass__(cls):
            PopulationGenerators.type.update({cls.__name__: cls})

        @classmethod
        def generate(cls, chromosome_type: BaseChromosome, gen_type: BaseGen, individual_type: BaseIndividual):
            LoggerHandler.error(cls.__name__, f"You must add a generate() definition for '{cls.__name__}'.")