import random
from Genetic.Gen import GEN_STATE

class Mutation:
    MUTATION_RATE = 0

    @classmethod
    def apply(cls, chromosome):
        selected_removed = chromosome.getSelectedFeaturesSize() / chromosome.getRemovedFeaturesSize()

        removed_mutation_rate = Mutation.MUTATION_RATE
        selected_mutation_rate = Mutation.MUTATION_RATE * selected_removed

        for gen in chromosome:
            threshold = random.random()
            if gen == GEN_STATE.SELECTED and removed_mutation_rate < removed_mutation_rate:
                gen.alterGen()
            elif gen == GEN_STATE.REMOVED and threshold < selected_mutation_rate:
                gen.alterGen()
