from Genetic.Chromosome import BaseChromosome
from Genetic.Individual import *


class AgedIndividual(BaseIndividual):

    def __init__(self, chromosome: BaseChromosome):
        super().__init__(chromosome)
        self.age: int = 0

    def incrementAge(self):
        self.age += 1

    def resetAge(self):
        self.age = 0

