from __future__ import annotations
import numpy as np
from Genetic.Individual import *
from Genetic.Chromosome import *


class ChromosomeDistribution:

    IDEAL_CHROMOSOME_DISTRIBUTION: ChromosomeDistribution = None

    def __init__(self, ideal_chromosome_distribution: dict):
        self.__ideal_chromosome_distribution__: dict = ideal_chromosome_distribution

    def __sub__(self, other) -> dict:
        if not isinstance(other, ChromosomeDistribution):
            raise TypeError(f"You must minus two {__name__}")

        diff = {}
        for category in self.__ideal_chromosome_distribution__:
            diff[category] = self.__ideal_chromosome_distribution__[category] - \
                             other.__ideal_chromosome_distribution__[category]
        return diff

    def distance(self, other) -> int:
        return np.abs(np.sum(np.array(list(self.__ideal_chromosome_distribution__.values())) -
                      np.array(list(other.__ideal_chromosome_distribution__.values()))))

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
    def distance(individual_1: BaseIndividual, individual_2: BaseIndividual) -> int:
        chromosome_1_distribution = ChromosomeDistribution.__from_individual__(individual_1)
        chromosome_2_distribution = ChromosomeDistribution.__from_individual__(individual_2)

        return chromosome_1_distribution.distance(chromosome_2_distribution)