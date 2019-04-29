from Genetic.Gen import Gen, GEN_STATE


class Chromosome:

    gens = []

    def __init__(self, size = 0, gens = []):
        if(len(gens) == 0):
            self.gens = [Gen() for _ in range(size)]
        else:
            self.gens = [Gen(gen) for gen in gens]

    def addFeatureAt(self, index):
        self.gens[index].selectGen()

    def removeFeatureAt(self, index):
        self.gens[index].removeGen()

    def getFeatureAt(self, index):
        return self.gens[index].state

    def getSelectedFeatures(self):
        selected_features = [index for index in range(len(self.gens)) if
                             self.gens[index].state == GEN_STATE.SELECTED]
        return selected_features

    def getRemovedFeatures(self):
        removed_features = [index for index in range(len(self.gens)) if
                            self.gens[index].state == GEN_STATE.REMOVED]
        return removed_features

    def getChromosome(self):
        return self.gens

    def getSelectedFeaturesSize(self):
        selected_features = [index for index in range(len(self.gens)) if
                             self.gens[index].state == GEN_STATE.SELECTED]
        return len(selected_features)

    def getRemovedFeaturesSize(self):
        removed_features = [index for index in range(len(self.gens)) if
                            self.gens[index].state == GEN_STATE.REMOVED]
        return len(removed_features)

    def __len__(self):
        return len(self.gens)

    def __getitem__(self, index):
        if isinstance(index, slice) and index.start == index.stop:
            list = [gen.state for gen in self.gens[index.start:index.stop + 1]]
        else:
            list = [gen.state for gen in self.gens[index]]

        return list

    def __setitem__(self, index, value):
        if isinstance(index, slice) and index.start == index.stop:
            self.gens[index.start:index.stop + 1] = [Gen(gen) for gen in value]
        else:
            self.gens[index] = [Gen(gen) for gen in value]

    def __repr__(self):
        return str([gen for gen in self.gens])

    def __str__(self):
        return str([gen for gen in self.gens])

    @property
    def lenght(self):
        return len(self.gens)