from Log import LoggerHandler
from Genetic.Components import Individual, Population, Chromosome
from Genetic.ReplacementMethods import ReplacementMethods
from EmailParser import DataCategory

class SelectiveReplacement(ReplacementMethods):

    @classmethod
    def __hamming_distance__(cls, offspring: Individual, parent: Individual, dataCategory: DataCategory):
        parent_words = {}
        offspring_words = {}

        for category in dataCategory:
            parent_words[category.categoryName] =  parent.getWordsFromIndividual(category)
            offspring_words[category.categoryName] = offspring.getWordsFromIndividual(category)


        # Start with a distance of zero, and count up
        distance = 0

        for category in offspring_words:
            # Loop over the indices of the string
            L = len(offspring_words[category])
            for i in range(L):
                # Add 1 to the distance if these two characters are not equal
                if i >= len(offspring_words[category]) or i >= len(parent_words[category]) or offspring_words[category][i] != parent_words[category][i]:
                    distance += 1

        return distance

    @classmethod
    def replacement(cls, parent_1: Individual, parent_2: Individual, offspring: Individual, population: [Individual], dataCategory: DataCategory):
        if parent_1.score <= offspring.score >= parent_2.score:
            distance_to_parent_1 = SelectiveReplacement.__hamming_distance__(offspring, parent_1, dataCategory)
            distance_to_parent_2 = SelectiveReplacement.__hamming_distance__(offspring, parent_2, dataCategory)

            if distance_to_parent_1 >= distance_to_parent_2:
                population.pop(population.index(parent_1))
                population.append(offspring)
            else:
                population.pop(population.index(parent_2))
                population.append(offspring)

        elif parent_1.score >= offspring.score >= parent_2.score or parent_1.score <= offspring.score <= parent_2.score:
            distance_to_parent_1 = SelectiveReplacement.__hamming_distance__(offspring, parent_1, dataCategory)
            distance_to_parent_2 = SelectiveReplacement.__hamming_distance__(offspring, parent_2, dataCategory)

            if distance_to_parent_1 >= distance_to_parent_2:
                population.pop(population.index(parent_2))
                population.append(offspring)
            else:
                population.pop(population.index(parent_1))
                population.append(offspring)

        else:
            population.sort(key=lambda individual: individual.score, reverse=True)
            population.pop(-1)
            population.append(offspring)


