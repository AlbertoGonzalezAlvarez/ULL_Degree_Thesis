from Genetic.Chromosome import Chromosome
from Genetic.Fitness import Fitness

class Individual():

    MAX_INDIVIDUAL_FEATURES = 0

    def __init__(self, lenght: int = 0):
        self.chromosome = Chromosome(size = lenght)
