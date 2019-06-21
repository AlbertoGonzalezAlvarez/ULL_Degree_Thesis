#TODO: poblacion en el algoritmo genetico como un vector, no representarlo con una clase


from Genetic.Individual import *
from Genetic.PopulationUpdaters.Updaters import *

#deprecated
class BasePopulation:

    POPULATION_UPDATE_METHOD: type = None

    def __init__(self, population: [BaseIndividual]):
        self.population: [BaseIndividual] = population

    def update_population(self):
        BasePopulation.POPULATION_UPDATE_METHOD.update(self.actual_population, self.next_population)