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

    def chromosomeDocuments(self) -> [str]:
        categories = {gen.category for gen in self.__selected_gens__}

        map_of_documents = {}
        for category in categories:
            map_of_documents[category] = ""

        for gen in self.__selected_gens__:
            map_of_documents[gen.category] += gen.word

        return [map_of_documents.values()]

    def chromosomeCategories(self) -> [str]:
        return list({gen.category for gen in self.__selected_gens__})

    def is_selected(self, gen: BaseGen) -> bool:
        return gen in self.__selected_gens__

    @property
    def selected_gens_size(self) -> int:
        return len(self.__selected_gens__)

    @property
    def removed_gens_size(self) -> int:
        return len(self.__removed_gens__)

    @property
    def selected_gens(self):
        return self.__selected_gens__

    def unselect(self, gen: BaseGen):
        self.__selected_gens__.pop(self.__selected_gens__.index(gen))
        self.__removed_gens__.append(gen)

    def select(self, gen: BaseGen):
        self.__selected_gens__.append(self.__selected_gens__.index(gen))
        self.__removed_gens__.pop(gen)