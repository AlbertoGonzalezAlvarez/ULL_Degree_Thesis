from Genetic.Chromosome import *
from Genetic.Gen import *

class BaseChromosome(ChromosomeTypes):

    def __init__(self, selected_gens_by_category: [BaseGen], removed_gens_by_category: [BaseGen]):
        self.__selected_gens__: [BaseGen] = selected_gens_by_category
        self.__removed_gens__: [BaseGen] = removed_gens_by_category
        self.__current_gen__ = 0

    @staticmethod
    def generateChromosome():
        # Generamos el objeto BaseChromosome y lo retornamos
        pass

    def __iter__(self):
        return self

    def __next__(self) -> BaseGen:
        if self.__current_gen__ > self.__selected_gens_length__:
            raise StopIteration

        self.__current_gen__ += 1
        return self.__selected_gens__[self.__current_gen__ - 1]

    def __len__(self):
        return len(self.__selected_gens__) + len(self.__removed_gens__)