from Log import *
from Genetic.Chromosome import *
from Genetic.Gen import *
from Genetic.Individual import *
from EmailParser.DataCategory import *
import copy


class PopulationGenerator:

        LOWEST_PERCENTAGE_VALUE: float = 0.0
        UPPER_PERCENTAGE_VALUE: float = 1.0
        type = {}

        def __init_subclass__(cls):
            PopulationGenerator.type.update({cls.__name__: cls})

        @classmethod
        def generate(cls, generator_type: str, chromosome_type: BaseChromosome, gen_type: BaseGen,
                     individual_type: BaseIndividual, population_size: int, train_data: [DataCategory],
                     percentage_of_features: int = -1) -> [BaseIndividual]:

            if cls.LOWEST_PERCENTAGE_VALUE < percentage_of_features < cls.UPPER_PERCENTAGE_VALUE:
                LoggerHandler.error(__name__, f"Percentage of features must be between [{cls.LOWEST_PERCENTAGE_VALUE} , "
                f"{cls.UPPER_PERCENTAGE_VALUE}]")

            train_data_copy: [DataCategory] = copy.deepcopy(train_data)
            list_of_gens_per_category: dict = gen_type.generate_gens_from_data(train_data_copy)

            category_lenghts = {category.name: len(category) for category in train_data}
            ChromosomeDistribution.IDEAL_CHROMOSOME_DISTRIBUTION = ChromosomeDistribution(category_lenghts)

            return PopulationGenerator.type[generator_type].generate_individuals(individual_type, chromosome_type,
                                                                                 list_of_gens_per_category, population_size,
                                                                                 category_lenghts, percentage_of_features)