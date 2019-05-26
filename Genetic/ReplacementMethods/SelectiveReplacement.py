from Log import LoggerHandler
from Genetic.Components import Individual, Population, Chromosome
from Genetic.ReplacementMethods import ReplacementMethods

class SelectiveReplacement(ReplacementMethods):

    @classmethod
    def __hamming_distance__(cls, chromosome_1: Chromosome, chromosome_2: Chromosome):
        # Start with a distance of zero, and count up
        distance = 0
        # Loop over the indices of the string
        L = len(chromosome_1)
        for i in range(L):
            # Add 1 to the distance if these two characters are not equal
            if chromosome_1[i] != chromosome_2[i]:
                distance += 1
        # Return the final count of differences
        return distance

    @classmethod
    def calculateNextPopulation(cls, parent_1: Individual, parent_2: Individual, offspring: Individual, population: Population):
        if parent_1.score <= offspring.score >= parent_2.score:
            distance_to_parent_1 = SelectiveReplacement.__hamming_distance__(offspring.chromosome, parent_1.chromosome)
            distance_to_parent_2 = SelectiveReplacement.__hamming_distance__(offspring.chromosome, parent_2.chromosome)

            if distance_to_parent_1 >= distance_to_parent_2:
                population.replace(parent_1, offspring)
            else:
                population.replace(parent_2, offspring)

        elif parent_1.score >= offspring.score >= parent_2.score or parent_1.score <= offspring.score <= parent_2.score:
            distance_to_parent_1 = SelectiveReplacement.__hamming_distance__(offspring.chromosome, parent_1.chromosome)
            distance_to_parent_2 = SelectiveReplacement.__hamming_distance__(offspring.chromosome, parent_2.chromosome)

            if distance_to_parent_1 >= distance_to_parent_2:
                population.replace(parent_2, offspring)
            else:
                population.replace(parent_1, offspring)

        else:
            index_to_remove = population.individualIndex(population.getNFirstIndividuals(-1))
            population.pop(index_to_remove)
            population.push(offspring)


