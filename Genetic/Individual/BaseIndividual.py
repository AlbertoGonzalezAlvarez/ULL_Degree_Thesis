from Genetic.Chromosome import BaseChromosome
from Genetic.Individual import *
from Genetic.Gen import *

class BaseIndividual(IndividualTypes):
    def __init__(self, chromosome: BaseChromosome):
        self.chromosome: BaseChromosome = chromosome
        self.score: float = 0.0

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score