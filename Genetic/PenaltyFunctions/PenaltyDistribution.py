from Genetic.PenaltyFunctions import *
from Genetic.Individual import *
from Genetic.Chromosome import  *


class PenaltyDistribution(PenaltyFunctions):

    @staticmethod
    def penalize(individual: BaseIndividual, penalty: float):
        diff: int = ChromosomeDistribution.distance_from_ideal(individual)
        individual.score = individual.score - penalty * diff