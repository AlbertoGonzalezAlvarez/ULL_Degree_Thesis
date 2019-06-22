from Genetic.PopulationUpdaters import PopulationUpdaters
from Genetic.Individual import BaseIndividual


class SimpleSwapper(PopulationUpdaters):
    @staticmethod
    def update(actual_population: [BaseIndividual], next_population: [BaseIndividual]) -> [BaseIndividual]:
        return next_population