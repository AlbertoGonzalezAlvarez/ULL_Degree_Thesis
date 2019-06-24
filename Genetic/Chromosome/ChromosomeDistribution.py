from __future__ import annotations
import numpy as np
from Genetic.Individual import *
from Genetic.Chromosome import *


class ChromosomeDistribution:

    IDEAL_CHROMOSOME_DISTRIBUTION: ChromosomeDistribution = None

    def __init__(self, ideal_chromosome_distribution: dict):
        self.chromosome_distribution: dict = ideal_chromosome_distribution

    def __sub__(self, other) -> dict:
        if not isinstance(other, ChromosomeDistribution):
            raise TypeError(f"You must minus two {__name__}")

        diff = {}
        for category in self.chromosome_distribution:
            diff[category] = self.chromosome_distribution[category] - \
                             other.chromosome_distribution[category]
        return diff

    def distance(self, other) -> int:
        # Take care, probably negative values are possible
        return np.sum(np.array(list(self.chromosome_distribution.values())) -
                      np.array(list(other.chromosome_distribution.values())))

    @staticmethod
    def __from_individual__(individual: BaseIndividual):
        chromosome: BaseChromosome = individual.chromosome

        chromosome_distribution: dict = {}

        for category in chromosome.chromosomeCategories():
            chromosome_distribution[category] = 0

        for gen in chromosome.selected_gens:
            chromosome_distribution[gen.category] += 1

        return ChromosomeDistribution(chromosome_distribution)

    @staticmethod
    def absolute_distance(individual_1: BaseIndividual, individual_2: BaseIndividual) -> int:
        chromosome_1_distribution = ChromosomeDistribution.__from_individual__(individual_1)
        chromosome_2_distribution = ChromosomeDistribution.__from_individual__(individual_2)

        return chromosome_1_distribution.distance(chromosome_2_distribution)

    @staticmethod
    def distance_from_ideal(individual_1: BaseIndividual) -> int:
        chromosome_1_distribution = ChromosomeDistribution.__from_individual__(individual_1)

        return np.abs(chromosome_1_distribution.distance(ChromosomeDistribution.IDEAL_CHROMOSOME_DISTRIBUTION))