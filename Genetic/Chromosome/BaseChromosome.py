class BaseChromosome:
    def __init__(self, selected_gens_by_category: dict, removed_gens_by_category:dict):
        self.__selected_gens_by_category__: dict = selected_gens_by_category
        self.__removed_gens_by_category__: dict = removed_gens_by_category