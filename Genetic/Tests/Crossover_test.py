import unittest
from Genetic.Operations.Crossover import Crossover
from Genetic.Chromosome import Chromosome
from Genetic.Gen import GEN_STATE as G

class TestCrossover(unittest.TestCase):
    parent_1 = Chromosome(gens = [G.REMOVED, G.REMOVED, G.REMOVED, G.REMOVED, G.REMOVED])
    parent_2 = Chromosome(gens = [G.SELECTED, G.REMOVED, G.SELECTED, G.REMOVED, G.SELECTED])

    def testApply(self):
        CROSSPOINTS = [2, 4]
        EXPECTED_VALUE = \
            [
                [G.REMOVED, G.REMOVED, G.SELECTED, G.REMOVED, G.REMOVED],
                [G.SELECTED, G.REMOVED, G.REMOVED, G.REMOVED, G.SELECTED]
            ]

        self.assertEqual(str(Crossover.apply(self.parent_1, self.parent_2, CROSSPOINTS)), str(EXPECTED_VALUE))


