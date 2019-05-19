import unittest
from Genetic.Operations.Crossover import Crossover
from Genetic.Chromosome import Chromosome
from Genetic.Gen import GEN_STATE as STATE
from Genetic.Gen import Gen


class TestCrossover(unittest.TestCase):
    parent_1 = Chromosome([], 4)
    parent_2 = Chromosome([0, 2, 4], 4)

    def testApply(self):
        CROSSPOINTS = [2, 4]
        EXPECTED_VALUE = \
            [
                [2],
                [0, 4]
            ]

        self.assertEqual(str(Crossover.apply(self.parent_1, self.parent_2, CROSSPOINTS)), str(EXPECTED_VALUE))