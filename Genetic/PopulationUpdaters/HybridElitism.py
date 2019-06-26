from Genetic.PopulationUpdaters import PopulationUpdaters
from Genetic.Individual import BaseIndividual


class HybridElitism(PopulationUpdaters):
    @staticmethod
    def update(actual_population: [BaseIndividual], next_population: [BaseIndividual]) -> [BaseIndividual]:
        real_next_population: [BaseIndividual] = sorted(actual_population + next_population, reverse=True)

        return [real_next_population[0]] + next_population[1:]
