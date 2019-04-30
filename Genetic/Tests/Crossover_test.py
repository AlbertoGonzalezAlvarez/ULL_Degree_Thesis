import unittest
from Genetic.Operations.Crossover import Crossover
from Genetic.Chromosome import Chromosome
from Genetic.Gen import GEN_STATE as STATE
from Genetic.Gen import Gen


class TestCrossover(unittest.TestCase):
    parent_1 = Chromosome(gens = [STATE.REMOVED, STATE.REMOVED, STATE.REMOVED, STATE.REMOVED, STATE.REMOVED])
    parent_2 = Chromosome(gens = [STATE.SELECTED, STATE.REMOVED, STATE.SELECTED, STATE.REMOVED, STATE.SELECTED])

    def testApply(self):
        CROSSPOINTS = [2, 4]
        EXPECTED_VALUE = \
            [
                [Gen(STATE.REMOVED), Gen(STATE.REMOVED), Gen(STATE.SELECTED), Gen(STATE.REMOVED), Gen(STATE.REMOVED)],
                [Gen(STATE.SELECTED), Gen(STATE.REMOVED), Gen(STATE.REMOVED), Gen(STATE.REMOVED), Gen(STATE.SELECTED)]
            ]

        self.assertEqual(str(Crossover.apply(self.parent_1, self.parent_2, CROSSPOINTS)), str(EXPECTED_VALUE))