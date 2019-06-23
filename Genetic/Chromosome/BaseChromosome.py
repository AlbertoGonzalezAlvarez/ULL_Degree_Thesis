from Genetic.Chromosome import *
from Genetic.Gen import *
import random


class BaseChromosome(ChromosomeTypes):

    def __init__(self, selected_gens_by_category: [BaseGen], removed_gens_by_category: [BaseGen]):
        # Improves computation time. Gens could be sets!!
        self.__selected_gens__: [BaseGen] = selected_gens_by_category
        self.__removed_gens__: [BaseGen] = removed_gens_by_category
        self.__current_gen__ = 0

        self.gens: [BaseGen] = random.shuffle(selected_gens_by_category + removed_gens_by_category)

    def __iter__(self):
        return self

    def __next__(self) -> BaseGen:
        if self.__current_gen__ > len(self.gens):
            raise StopIteration

        self.__current_gen__ += 1
        return self.gens[self.__current_gen__ - 1]

    def __len__(self):
        return len(self.gens)

    def __update_gens__(self):
        self.gens.clear()
        self.gens = random.shuffle(self.__selected_gens__ + self.__removed_gens__)

    @property
    def selected_gens_size(self) -> int:
        return len(self.__selected_gens__)

    @property
    def removed_gens_size(self) -> int:
        return len(self.__removed_gens__)

    @property
    def selected_gens(self):
        return self.__selected_gens__

    def is_selected(self, gen: BaseGen) -> bool:
        return gen in self.__selected_gens__

    def unselect(self, gen: BaseGen):
        self.__selected_gens__.pop(self.__selected_gens__.index(gen))
        self.__removed_gens__.append(gen)
        self.__update_gens__()

    def select(self, gen: BaseGen):
        # Maybe we're inserting a repeated gen?
        self.__selected_gens__.append(self.__selected_gens__.index(gen))
        self.__removed_gens__.pop(gen)
        self.__update_gens__()

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