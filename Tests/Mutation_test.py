import unittest
from copy import deepcopy
from Genetic.Operations.Mutation import Mutation
from Genetic.Chromosome import Chromosome


class TestMutation(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.CHRROMOSOME = Chromosome([1, 4], 4)

    def testYesMutation(self):
        CHROMOSOME_COPY = deepcopy(TestMutation.CHRROMOSOME)
        Mutation.MUTATION_RATE = 1
        Mutation.apply(TestMutation.CHRROMOSOME)

        self.assertNotEqual(CHROMOSOME_COPY, TestMutation.CHRROMOSOME)

    def testNoMutation(self):
        CHROMOSOME_COPY = TestMutation.CHRROMOSOME
        Mutation.MUTATION_RATE = 0
        Mutation.apply(CHROMOSOME_COPY)

        self.assertEqual(CHROMOSOME_COPY, TestMutation.CHRROMOSOME)