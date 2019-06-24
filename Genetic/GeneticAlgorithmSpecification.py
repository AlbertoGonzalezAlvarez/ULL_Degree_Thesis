from Genetic.PopulationUpdaters import *
from Genetic.PopulationGenerators import *
from Genetic.Individual import *
from Genetic.ParentSelector import *
from Genetic.Chromosome import *
from Genetic.Gen import *
from EmailParser.DataCategory import *


class GeneticAlgorithmSpecification:
    def __init__(self, crossover_prob: float, mutation_prob: float, train_data: [DataCategory], individual_max_len: int,
                 population_updater: str, population_generator: str, max_generations: int,
                 parent_selector: str, population_size: int):

        self.crossover_prob: float = crossover_prob
        self.mutation_prob: float = mutation_prob
        self.train_data: [DataCategory] = train_data
        self.max_generations: int = max_generations
        self.population_updater: PopulationUpdaters = PopulationUpdaters.type[population_updater]
        self.parent_selector: ParentSelector = ParentSelector.type[parent_selector]
        self.population: [BaseIndividual] = PopulationGenerator.type[population_generator].generate(
            generator_type=population_generator,
            chromosome_type=BaseChromosome.types["BaseChromosome"],
            gen_type=BaseGen.type["BaseGen"],
            individual_type=BaseIndividual.types["BaseIndividual"],
            population_size=population_size,
            train_data=train_data,
            percentage_of_features=individual_max_len
        )