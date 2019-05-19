from __future__ import annotations
from copy import copy, deepcopy
from Log.LoggerHandler import LoggerHandler
from Genetic.Gen import Gen, GEN_STATE
import numpy as np
from collections import OrderedDict

class Chromosome:

    def __init__(self, selectedGensIndex:set = set(), size:int = 0):
        if len(selectedGensIndex) > 0 and max(selectedGensIndex) > size:
            LoggerHandler.error(__name__, "You trying to insert a gen greather than chromosome lenght")

        self.iterLastIndex: int = 0
        self.puntuaction: float = 0.0
        self.size:int = size
        self.gens: list = []

        if(len(selectedGensIndex) > 0):
            self.gens = selectedGensIndex

    def alterGenAt(self, index) -> None:
        if index > self.size:
            raise IndexError(f"You are trying to add a feature at {index} and chromosome only have {self.size} gens")

        if index in self.gens:
            del self.gens[self.gens.index(index)]
        else:
            self.gens.append(index)

    def featureAt(self, element) -> Gen:
        if element > self.size:
            raise IndexError(f"You are trying to access gen at {element} and chromosome only have {self.size} gens")
        elif element not in self.getSelectedFeatures():
            return Gen(GEN_STATE.REMOVED)

        return Gen(GEN_STATE.SELECTED)

    def getSelectedFeatures(self) -> list[int]:
        return list(self.gens)

    def getRemovedFeatures(self) -> list[int]:
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

    def gensBetween(self, from_, stop) -> list[int]:
        if not(from_ <= self.size and  stop <= self.size):
            raise IndexError(f"You are trying to slice gen {from_} - {stop} and chromosome only have {self.size} gens")

        if from_ == stop:
            if stop in self.gens:
                return [self.gens[self.gens.index(stop)]]
            else:
                return []
        else:
            return [gen for gen in self.gens if from_ <= gen <= stop]

    def __getitem__(self, index) -> Gen:
        if isinstance(index, slice):
            return self.gensBetween(index.start, index.stop)
        else:
            return self.gensBetween(index, index)

    def __setitem__(self, index, value) -> None:
        if isinstance(index, slice):
            result = self.gens.copy()

            for gen in self.gens:
                if index.start <= gen <= index.stop:
                    del result[result.index(gen)]

            if isinstance(value, list):
                for gen in value:
                    if gen not in result:
                        result.append(gen)
            else:
                result.append(value)

            self.gens = result
        elif isinstance(value, list):
            result = self.gens.copy()
            if index in result:
                del result[result.index(index)]

            for gen in value:
                if gen not in result:
                    result.append(gen)

            self.gens = result

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

    def __len__(self):
        return self.size