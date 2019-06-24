from Genetic.PopulationUpdaters import PopulationUpdaters
from Genetic.Individual import BaseIndividual


class BestsIndividuals(PopulationUpdaters):
    @staticmethod
    def update(actual_population: [BaseIndividual], next_population: [BaseIndividual]) -> [BaseIndividual]:
        actual_population_ordered = sorted(actual_population, reverse=True)
        next_population_ordered = sorted(next_population, reverse=True)

        real_next_population = []
        actual_index = 0
        next_index = 0

        for _ in range(len(actual_population_ordered)):
            if actual_population_ordered[actual_index].score > next_population_ordered[next_index].score:
                real_next_population.append(actual_population_ordered[actual_index])
                actual_index += 1
            else:
                real_next_population.append(next_population_ordered[next_index])
                next_index += 1

        return real_next_population
