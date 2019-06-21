from Genetic.PopulationUpdaters import PopulationUpdaters
from Genetic.Individual import BaseIndividual


class BestsIndividuals(PopulationUpdaters):
    @staticmethod
    def update(actual_population: [BaseIndividual], next_population: [BaseIndividual]) -> [BaseIndividual]:
        actual_population_ordered = sorted(actual_population)
        next_population_ordered = sorted(next_population)

        real_next_population = []

        for index in range(len(actual_population_ordered)):
            if actual_population_ordered[index].score > next_population_ordered.score:
                real_next_population.append(actual_population_ordered[index])
            else:
                real_next_population.append(next_population_ordered[index])

        return real_next_population