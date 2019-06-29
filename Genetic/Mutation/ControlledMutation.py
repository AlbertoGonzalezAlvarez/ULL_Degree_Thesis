from Genetic.Mutation import *
from Genetic.Individual import *
from Genetic.Chromosome import *
import random


class ControlledMutation(BaseMutation):
    @staticmethod
    def mutate(individual: BaseIndividual):
        chromosome: BaseChromosome = individual.chromosome

        prob_remove: float = ControlledMutation.RATE
        prob_insert: float = ControlledMutation.RATE * chromosome.selected_gens_size / chromosome.removed_gens_size

        for index in range(len(chromosome)):
            threshold = random.random()
            if threshold < prob_remove and chromosome.is_selected(index):
                chromosome.unselect(index)
            elif threshold < prob_insert and not chromosome.is_selected(index):
                chromosome.select(index)

        chromosome.update_gens()
