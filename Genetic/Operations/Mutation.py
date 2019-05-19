import random
from Genetic.Gen import GEN_STATE

class Mutation:
    MUTATION_RATE = 0

    @classmethod
    def apply(cls, chromosome):
        selected_removed = chromosome.getSelectedFeaturesSize() / chromosome.getRemovedFeaturesSize()

        removed_mutation_rate = Mutation.MUTATION_RATE
        selected_mutation_rate = Mutation.MUTATION_RATE * selected_removed

        for index in range(chromosome.lenght):
            threshold = random.random()
            if index in chromosome.gens and threshold < removed_mutation_rate:
                chromosome.alterGen(index)
            elif index not in chromosome.gens and threshold < selected_mutation_rate:
                chromosome.alterGen(index)

