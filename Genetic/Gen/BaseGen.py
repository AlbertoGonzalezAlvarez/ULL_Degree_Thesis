from Genetic.Gen import *


class BaseGen(GenTypes):

    def __init__(self, word: str, category: str):
        self.word = word
        self.category = category
