import unittest
from copy import copy, deepcopy
from Genetic.Operations.Mutation import Mutation
from Genetic.Chromosome import Chromosome
from Genetic.Gen import GEN_STATE as G

class TestMutation(unittest.TestCase):

    def setUp(self):
        self.CHRROMOSOME = Chromosome(gens=[G.REMOVED, G.SELECTED, G.REMOVED, G.REMOVED, G.SELECTED])

    def testYesMutation(self):
        CHROMOSOME_COPY = deepcopy(self.CHRROMOSOME)
        Mutation.MUTATION_RATE = 1
        Mutation.apply(self.CHRROMOSOME)

        self.assertNotEqual(CHROMOSOME_COPY, self.CHRROMOSOME)

    def testNoMutation(self):
        CHROMOSOME_COPY = self.CHRROMOSOME
        Mutation.MUTATION_RATE = 0
        Mutation.apply(CHROMOSOME_COPY)

        self.assertEqual(CHROMOSOME_COPY, self.CHRROMOSOME)