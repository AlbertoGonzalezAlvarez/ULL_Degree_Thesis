from Genetic.Mutation import *
from Genetic.Individual import *
from Genetic.Chromosome import *
import random


class FixedMutation(BaseMutation):
    @staticmethod
    def mutate(individual: BaseIndividual):
        chromosome: BaseChromosome = individual.chromosome

        prob_remove: float = ControlledMutation.RATE

        removed = 0
        for index in range(len(chromosome)):
            threshold = random.random()
            if threshold < prob_remove and chromosome.is_selected(index):
                chromosome.unselect(index)
                removed += 1

        while removed == 0:
            index = random.randint(0, len(chromosome.removed_gens))
            if not chromosome.is_selected(index):
                chromosome.select(index)
                removed -= 1

