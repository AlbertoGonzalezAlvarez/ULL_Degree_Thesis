from sklearn.feature_extraction.text import TfidfVectorizer
from EmailParser.DataCategory import DataCategory
from Genetic.Individual import Individual

class Fitness:

    @staticmethod
    def compute(test_data_corpus: DataCategory, population_words, individuals: Individual):

        for individual_index in range(len(individuals)):
            vectorizer = TfidfVectorizer(vocabulary = population_words[individual_index])
            result = vectorizer.fit_transform(test_data_corpus)

            feature_names = vectorizer.get_feature_names()

            for col in set(result.nonzero()[1]):
                if result[0, col] > 0.0:
                    print(feature_names[col], ' - ', result[0, col])


        return 0
