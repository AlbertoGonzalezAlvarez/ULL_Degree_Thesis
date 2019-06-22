from Genetic.Chromosome import *
from Genetic.Individual import *
from Genetic.Gen import *


class CategorizedIndividual(BaseIndividual):
    def __init__(self, chromosome: CategorizedChromosome):
        super().__init__(chromosome)
        self.chromosome: CategorizedChromosome = chromosome