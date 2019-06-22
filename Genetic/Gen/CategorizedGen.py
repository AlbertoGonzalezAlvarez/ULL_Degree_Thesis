from Genetic.Gen import *


class CategorizedGen(BaseGen):

    def __init__(self, word: str, category: str):
        super().__init__(word)
        self.category = category