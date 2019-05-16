from Genetic.Gen import Gen, GEN_STATE
from copy import copy, deepcopy
from Log.LoggerHandler import LoggerHandler
import numpy as np
import sys

class Chromosome:

    def __init__(self, selectedGensIndex:set = set(), size:int = 0):
        if len(selectedGensIndex) > 0 and max(selectedGensIndex) >= size:
            LoggerHandler.error(__name__, "You trying to insert a gen greather than chromosome lenght")

        self.iterLastIndex = 0
        self.puntuaction = 0
        self.size = size
        self.gens = {}

        if(len(selectedGensIndex) > 0):
            self.gens = Gen.getGensFromList(selectedGensIndex)


    def addFeatureAt(self, index, gen: Gen = None):
        if gen != None and isinstance(gen, Gen):
            self.gens[index] = gen
        else:
            self.gens[index] = Gen(GEN_STATE.REMOVED)

    def removeFeatureAt(self, index):
        del self.gens[index]

    def featureAt(self, index):
        if index > self.size:
            raise IndexError(f"You are trying to access gen at {index} and chromosome only have {self.size} gens")
        elif index not in self.gens:
            return Gen(GEN_STATE.REMOVED)

        return self.gens[index]

    def getSelectedFeatures(self):
        return list(self.gens.keys())

    def getRemovedFeatures(self):
        selected = set(self.getSelectedFeatures())
        all =  set(list(np.arange(self.size)))

        return list(all - selected)

    def getChromosome(self):
        return self.gens

    def getSelectedFeaturesSize(self):
        return len(self.gens)

    def getRemovedFeaturesSize(self):
        return self.size - self.getSelectedFeaturesSize()

    @property
    def lenght(self):
        return self.size

    def __getitem__(self, index):
        return self.featureAt(index)

    def __setitem__(self, index, value):
        if value != None and isinstance(value, Gen):
            self.addFeatureAt(index, value)

    def __repr__(self):
        return str(self.getSelectedFeatures())

    def __str__(self):
        return str(self.getSelectedFeatures())

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.featureAt(self.iterLastIndex)
        except IndexError:
            raise StopIteration
        self.iterLastIndex += 1
        return result

    def __eq__(self, other):
        if isinstance(other, Chromosome):
            return self.gens == other.gens
        else:
            return TypeError

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result