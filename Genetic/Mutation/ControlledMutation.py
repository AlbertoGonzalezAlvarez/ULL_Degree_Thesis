from Genetic.Mutation import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from Genetic.Gen import *
import random


class ControlledMutation(BaseMutation):
    @staticmethod
    def mutate(individual: BaseIndividual, mutation_rate: float):
        chromosome: BaseChromosome = individual.chromosome

        prob_remove: float = mutation_rate
        prob_insert: float = mutation_rate * chromosome.selected_gens_size / chromosome.removed_gens_size

        for index in range(len(chromosome)):
            threshold = random.random()
            if threshold < prob_remove and chromosome.is_selected(index):
                chromosome.unselect(index)
            elif threshold < prob_insert and not chromosome.is_selected(index):
                chromosome.select(index)

