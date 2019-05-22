import random
from Genetic.Components import Individual


class Mutation:
    MUTATION_RATE = 0

    @classmethod
    def apply(cls, individual: Individual) -> Individual:
        if (isinstance(individual, Individual)):
            new_individual = Individual(chromosome = individual.chromosome)

        new_individual_chromosome = new_individual.chromosome
        selected_removed = new_individual_chromosome.getSelectedFeaturesSize() / new_individual_chromosome.getRemovedFeaturesSize()

        removed_mutation_rate = Mutation.MUTATION_RATE
        selected_mutation_rate = Mutation.MUTATION_RATE * selected_removed

        for index in range(new_individual_chromosome.lenght):
            threshold = random.random()
            if index in new_individual_chromosome.gens and threshold < removed_mutation_rate:
                new_individual_chromosome.alterGen(index)
            elif index not in new_individual_chromosome.gens and threshold < selected_mutation_rate:
                new_individual_chromosome.alterGen(index)

        return new_individual