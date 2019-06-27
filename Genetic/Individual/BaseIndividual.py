from Genetic.Chromosome import BaseChromosome
from Genetic.Gen import *
from Genetic.Individual import *
import json


class BaseIndividual(IndividualTypes):
    def __init__(self, chromosome: BaseChromosome):
        self.chromosome: BaseChromosome = chromosome
        self.score: float = 0.0

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __repr__(self):
        return {
            "selected_gens": str(self.chromosome.selected_gens),
            "score": str(self.score)
        }

class BaseIndividualEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, BaseIndividual):
            words = []
            for gen in object.chromosome.selected_gens:
                words.append(BaseGenEncoder.default(self, gen))

            return {
                "words": words,
                "score": object.score
            }
        else:
            return json.JSONEncoder.default(self, object)