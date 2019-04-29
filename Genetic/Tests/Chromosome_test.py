import unittest
from Genetic.Chromosome import Chromosome
from Genetic.Gen import GEN_STATE, Gen


class TestChromosome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestChromosome.test_chromosome = Chromosome(10)

    def testChromosomeInit(self):
        EXPECTED_VALUE = ([GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.REMOVED])
        init_chromosome = Chromosome(gens = [GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.REMOVED])
        self.assertEqual(str(init_chromosome), str(EXPECTED_VALUE))

    def testChromosomeInitSize(self):
        EXPECTED_VALUE = 10
        self.assertEqual(self.test_chromosome.lenght, EXPECTED_VALUE)

    def testgetFeatureAt(self):
        EXPECTED_VALUE = GEN_STATE.REMOVED
        self.assertEqual(self.test_chromosome.getFeatureAt(9), EXPECTED_VALUE)

    def testAddFeatureAt(self):
        EXPECTED_VALUE = GEN_STATE.SELECTED
        self.test_chromosome.addFeatureAt(4)
        self.assertEqual(self.test_chromosome.getFeatureAt(4), EXPECTED_VALUE)

    def testRemoveFeatureAt(self):
        EXPECTED_VALUE = GEN_STATE.REMOVED
        self.test_chromosome.addFeatureAt(8)
        self.test_chromosome.removeFeatureAt(8)
        self.assertEqual(self.test_chromosome.getFeatureAt(8), EXPECTED_VALUE)

    def testGetSelectedFeatures(self):
        EXPECTED_VALUE = 1
        self.assertEqual(len(self.test_chromosome.getSelectedFeatures()), EXPECTED_VALUE)

    def testGetRemovedFeatures(self):
        EXPECTED_VALUE = 9
        self.assertEqual(len(self.test_chromosome.getRemovedFeatures()), EXPECTED_VALUE)

    def testGetChromosome(self):
        EXPECTED_VALUE = 10
        self.assertEqual(self.test_chromosome.lenght, EXPECTED_VALUE)

    def testChromosomeSlice(self):
        EXPECTED_VALUE = [GEN_STATE.REMOVED, GEN_STATE.REMOVED, GEN_STATE.SELECTED]
        self.assertEqual(self.test_chromosome[2:5], EXPECTED_VALUE)

    def testReplaceRange(self):
        EXPECTED_VALUE = [GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.SELECTED]
        self.test_chromosome[2:5] = [GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.SELECTED]
        self.assertEqual(self.test_chromosome[2:5], EXPECTED_VALUE)

    def testGetRemovedFeaturesSize(self):
        CHROMOSOME = Chromosome(gens=[GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.REMOVED])
        EXPECTED_VALUE = 1

        self.assertEqual(CHROMOSOME.getRemovedFeaturesSize(), EXPECTED_VALUE)

    def testSelectedFeaturesSize(self):
        CHROMOSOME = Chromosome(gens=[GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.SELECTED, GEN_STATE.REMOVED])
        EXPECTED_VALUE = 3

        self.assertEqual(CHROMOSOME.getSelectedFeaturesSize(), EXPECTED_VALUE)


if __name__ == '__main__':
    unittest.main()