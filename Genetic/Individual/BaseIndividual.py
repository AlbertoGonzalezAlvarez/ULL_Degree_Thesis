from Genetic.Chromosome import BaseChromosome
from Genetic.Gen import BaseGen


class BaseIndividual:
    def __init__(self, chromosome: BaseChromosome):
        self.__chromosome__: BaseChromosome = chromosome
        self.score: float =  0.0

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score