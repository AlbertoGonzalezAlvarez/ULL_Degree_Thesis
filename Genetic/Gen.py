from enum import Enum
import collections

class GEN_STATE(Enum):
    SELECTED, REMOVED = 1, 0

class Gen:
    gen_state = None

    def __init__(self, state: type = GEN_STATE.SELECTED):
        self.word = ""
        if state == None:
            self.gen_state = GEN_STATE.REMOVED
        else:
            self.gen_state = state

    def updateWord(self, word):
        self.word = word

    def selectGen(self):
        self.gen_state = GEN_STATE.SELECTED

    def removeGen(self):
        self.gen_state = GEN_STATE.REMOVED

    def alterGen(self):
        if (self.gen_state == GEN_STATE.SELECTED):
            self.gen_state = GEN_STATE.REMOVED
        else:
            self.gen_state = GEN_STATE.SELECTED

    def __str__(self):
        return  self.gen_state.name

    def __repr__(self):
        return  self.gen_state.name

    def __eq__(self, other):
        if isinstance(other, Gen):
            return self.state == other.state
        elif isinstance(other, GEN_STATE):
            return self.state == other
        else:
            return TypeError

    @staticmethod
    def getGensFromList(genSet: set = []):
        sparse_gen_vector = {}
        for genIndex in genSet:
            sparse_gen_vector[genIndex] = Gen(GEN_STATE.SELECTED)

        return collections.OrderedDict(sorted(sparse_gen_vector.items()))


    # print(genSet)
    # genList = list(genSet)
    # genList.sort()
    #
    # sparse_gen_vector = {}
    # for genIndex in genList:
    #     sparse_gen_vector[genIndex] = Gen(GEN_STATE.SELECTED)
    #
    # collections.OrderedDict(sorted(sparse_gen_vector.items()))
    # return sparse_gen_vector

    @property
    def state(self):
        return self.gen_state
