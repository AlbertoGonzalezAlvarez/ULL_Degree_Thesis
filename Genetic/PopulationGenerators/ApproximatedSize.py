import Utilities
from Genetic.Chromosome import *
from Genetic.Gen import *
from Genetic.Individual import *
from Genetic.PopulationGenerators import *
import random
import copy

class ApproximatedSize(PopulationGenerator):

    @staticmethod
    def generate_individuals(individual_type: BaseIndividual, chromosome_type: BaseChromosome,
                             list_of_gens_per_category: dict, population_size: int, category_lenghts: dict,
                             percentage_of_features: int = -1) -> [BaseIndividual]:

        population: [BaseIndividual] = []

        for _ in range(population_size):
            selected_gens_per_category: [BaseGen] = {category_name: [] for category_name in category_lenghts.keys()}

            for category in category_lenghts:
                gens_per_category: int = category_lenghts[category] * percentage_of_features
                threshold = gens_per_category / category_lenghts[category]

                for index, _ in enumerate(list_of_gens_per_category[category]):
                    if random.uniform(0, 1) < threshold:
                        selected_gens_per_category[category].append(list_of_gens_per_category[category].pop(index))

            # Merge removed and selected gens per category respectively
            removed_gens: [BaseGen] = []
            selected_gens: [BaseGen] = []

            for category in list(list_of_gens_per_category.keys()):
                removed_gens += list_of_gens_per_category[category]
                selected_gens += selected_gens_per_category[category]

            chromosome: BaseChromosome = chromosome_type(selected_gens[:], removed_gens[:])
            population.append(individual_type(chromosome))

            # Restore initial state of list of gens
            for category in selected_gens_per_category:
                list_of_gens_per_category[category] += selected_gens_per_category[category]
                random.shuffle(list_of_gens_per_category[category])

            selected_gens_per_category.clear()
            removed_gens.clear()
            selected_gens.clear()

        return population