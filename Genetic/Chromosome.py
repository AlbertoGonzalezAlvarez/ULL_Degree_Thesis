from __future__ import annotations
from Genetic.Gen import Gen, GEN_STATE
from copy import copy, deepcopy
from Log.LoggerHandler import LoggerHandler
import numpy as np
from collections import OrderedDict
import sys

class Chromosome:

    def __init__(self, selectedGensIndex:set = set(), size:int = 0):
        if len(selectedGensIndex) > 0 and max(selectedGensIndex) > size:
            LoggerHandler.error(__name__, "You trying to insert a gen greather than chromosome lenght")

        self.iterLastIndex: int = 0
        self.puntuaction: float = 0.0
        self.size:int = size
        self.gens: dict = {}

        if(len(selectedGensIndex) > 0):
            self.gens = Gen.getGensFromList(selectedGensIndex)


    def addFeatureAt(self, index, gen: Gen = None) -> None:
        if index > self.size:
            raise IndexError(f"You are trying to add a feature at {index} and chromosome only have {self.size} gens")

        if isinstance(gen, Gen):
            self.gens[index] = gen
        else:
            self.gens[index] = Gen(GEN_STATE.SELECTED)

    def removeFeatureAt(self, index) -> list[Gen]:
        del self.gens[index]

    def featureAt(self, index) -> Gen:
        if index > self.size:
            raise IndexError(f"You are trying to access gen at {index} and chromosome only have {self.size} gens")
        elif index not in self.gens:
            return Gen(GEN_STATE.REMOVED)

        return self.gens[index]

    def getSelectedFeatures(self) -> list[Gen]:
        return list(self.gens.keys())

    def getRemovedFeatures(self) -> list[Gen]:
        selected = set(self.getSelectedFeatures())
        all =  set(list(np.arange(self.size)))

        return list(all - selected)

    def getChromosome(self) -> OrderedDict[Gen]:
        return self.gens

    def getSelectedFeaturesSize(self) -> int:
        return len(self.gens)

    def getRemovedFeaturesSize(self) -> int:
        return self.size - self.getSelectedFeaturesSize()

    @property
    def lenght(self) -> int:
        return self.size

    # temporal
    def __getitem__(self, index) -> Gen:
        if isinstance(index, slice) and index.start == index.stop:
            list = [gen for gen in self.gens[index.start:index.stop + 1]]
        else:
            list = [gen for gen in self.gens[index]]

        return list

    def __setitem__(self, index, value) -> None:
        if value != None and isinstance(value, Gen):
            self.addFeatureAt(index, value)

    def __repr__(self) -> str(Gen):
        return str(self.getSelectedFeatures())

    def __str__(self) -> str(Gen):
        return str(self.getSelectedFeatures())

    def __iter__(self) -> Chromosome:
        return self

    def __next__(self) -> Gen:
        try:
            result = self.featureAt(self.iterLastIndex)
        except IndexError:
            raise StopIteration
        self.iterLastIndex += 1
        return result

    def __eq__(self, other) -> bool:
        if isinstance(other, Chromosome):
            return self.gens == other.gens
        else:
            return TypeError

    def __copy__(self) -> Gen:
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo) -> Gen:
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result