from __future__ import annotations
from Genetic.Chromosome import *
from Genetic.Gen import *
import random
import numpy as np
import json


class BaseChromosome(ChromosomeTypes):

    IDEAL_CHROMOSOME_DISTRIBUTION: dict = None
    LIST_OF_GENS: dict = None

    def __init__(self, selected_gens_by_category: [BaseGen], removed_gens_by_category: [BaseGen]):
        # Improves computation time. Gens could be sets!!
        self.__selected_gens__: [BaseGen] = selected_gens_by_category
        self.__removed_gens__: [BaseGen] = removed_gens_by_category
        self.__current_gen__ = 0
        self.gens: [BaseGen] = []
        self.__update_gens__()

    def __iter__(self):
        return self

    def __next__(self) -> BaseGen:
        if self.__current_gen__ > len(self.gens) - 1:
            raise StopIteration

        self.__current_gen__ += 1
        return self.gens[self.__current_gen__ - 1]

    def __len__(self):
        return len(self.gens)

    def __repr__(self):
        return str(self.__selected_gens__)

    def __update_gens__(self):
        self.gens.clear()
        self.gens = self.__selected_gens__ + self.__removed_gens__
        random.shuffle(self.gens)

    @property
    def selected_gens_size(self) -> int:
        return len(self.__selected_gens__)

    @property
    def removed_gens_size(self) -> int:
        return len(self.__removed_gens__)

    @property
    def selected_gens(self):
        return self.__selected_gens__

    @property
    def removed_gens(self):
        return self.__removed_gens__

    def is_selected(self, gen: BaseGen) -> bool:
        return gen in self.__selected_gens__

    def is_selected(self, index: int) -> bool:
        return index < self.selected_gens_size

    def unselect(self, gen: BaseGen):
        self.__selected_gens__.pop(self.__selected_gens__.index(gen))
        self.__removed_gens__.append(gen)
        # self.__update_gens__()

    def select(self, gen: BaseGen):
        # Maybe we're inserting a repeated gen?
        self.__selected_gens__.append(gen)
        self.__removed_gens__.pop(self.__removed_gens__.index(gen))
        # self.__update_gens__()

    def unselect(self, gen_index: int):
        #Can cause error
        gen: BaseGen = self.__selected_gens__.pop(gen_index)
        self.__removed_gens__.append(gen)
        # self.__update_gens__()

    def select(self, gen_index: int):
        gen: BaseGen = self.__removed_gens__.pop(gen_index - self.selected_gens_size)
        self.__selected_gens__.append(gen)
        # self.__update_gens__()

    def chromosomeDocuments(self) -> [str]:
        categories = self.chromosomeCategories()

        map_of_documents = {category_name: "" for category_name in categories}

        for gen in self.__selected_gens__:
            map_of_documents[gen.category] += gen.word + " "

        return list(map_of_documents.values())

    def chromosomeCategories(self) -> [str]:
        return sorted(list(BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION.keys()))

    def chromosome_distribution(self):
        chromosome_distribution: dict = {category: [] for category in
                                         BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION}

        for gen in self.selected_gens:
            chromosome_distribution[gen.category].append(gen.word)

        return chromosome_distribution

    @staticmethod
    def __absolut_distance__(chromosome_1: dict, chromosome_2: dict) -> int:
        difference_array: list = np.array(list(chromosome_1.values())) - \
                                 np.array(list(chromosome_2.values()))

        return [np.abs(value) for value in difference_array]

    def __compute_distribution__(self):
        chromosome_distribution: dict = {category: 0 for category in
                                         BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION}

        for gen in self.selected_gens:
            chromosome_distribution[gen.category] += 1

        return chromosome_distribution


    def distance_from_ideal(self) -> int:
        chromosome_distribution = self.__compute_distribution__()

        return BaseChromosome.__absolut_distance__(chromosome_distribution,
                                                   BaseChromosome.IDEAL_CHROMOSOME_DISTRIBUTION)

    @staticmethod
    def distance_between(chromosome_1: BaseChromosome, chromosome_2: BaseChromosome):
        chromosome_distribution_1: BaseChromosome = chromosome_1.__compute_distribution__()
        chromosome_distribution_2: BaseChromosome = chromosome_2.__compute_distribution__()

        return BaseChromosome.__absolut_distance__(chromosome_distribution_1, chromosome_distribution_2)

    @staticmethod
    def __distance__(chromosome_1: dict, chromosome_2: dict) -> int:
        difference_array: list = np.array(list(chromosome_1.values())) - \
                                 np.array(list(chromosome_2.values()))

        return difference_array


class BaseChromosomeEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, BaseChromosome):
            return BaseGenEncoder(self, object.selected_gens)
        else:
            return json.JSONEncoder.default(self, object)
