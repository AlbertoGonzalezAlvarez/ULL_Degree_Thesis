from Genetic.Gen import *
from Genetic.Chromosome import *


class CategorizedChromosome(BaseChromosome):
    def __init__(self, selected_gens_by_category: [CategorizedGen], removed_gens_by_category: [CategorizedGen]):
        super().__init__(selected_gens_by_category, removed_gens_by_category)

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