from Genetic.Gen import BaseGen, GenTypes
from EmailParser.DataCategory import *


class BaseGen(GenTypes):

    def __init__(self, word: str, category: str):
        self.word = word
        self.category = category

    @staticmethod
    def generate_gens_from_data(train_data: [DataCategory]) -> dict:
        list_of_gens: dict = {}

        for category in train_data:
            list_of_gens[category.name] = []

        for category in train_data:
            for word in category.corpus:
                list_of_gens[category.name].append(BaseGen(word, category.name))

        return list_of_gens

    def __eq__(self, other):
        return self.word == other.word and self.category == other.category

    def __repr__(self):
        return f"'{self.category}': {self.word}"