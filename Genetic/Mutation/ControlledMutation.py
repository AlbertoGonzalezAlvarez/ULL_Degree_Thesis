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

        for gen in chromosome:
            threshold = random.random()
            if chromosome.is_selected(gen) and threshold < prob_remove:
                chromosome.unselect(gen)
            elif not chromosome.is_selected(gen) and threshold < prob_insert:
                chromosome.select(gen)

