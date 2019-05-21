from sklearn.feature_extraction.text import TfidfVectorizer
from EmailParser.DataCategory import DataCategory
from Genetic.Individual import Individual

class Fitness:

    PENALIZATION_COEFFICIENT = 0.0
    TFIDF = {}

    @staticmethod
    def compute(current_category_name: str, individuals_words, individuals: Individual):
        individuals_score = {}

        for category in Fitness.TFIDF:
            individuals_score[category] = []
            for individual_index in range(len(individuals)):
                probabilities_of_words = []
                for word in individuals_words[individual_index]:
                    if word in Fitness.TFIDF[category]:
                        probabilities_of_words.append(Fitness.TFIDF[category][word])
                    else:
                        probabilities_of_words.append(0)
                individuals_score[category].append(sum(probabilities_of_words) / len(individuals_words[individual_index]))

        # Penalization
        max_category_probability_scores = individuals_score[current_category_name]
        max_category_probability_name = current_category_name

        for category in individuals_score:
            if sum(individuals_score[category]) > sum(max_category_probability_scores):
                max_category_probability_scores = individuals_score[category]
                max_category_probability_name = category

        for individual_index_score in range(len(individuals_score[current_category_name])):
            score = individuals_score[current_category_name][individual_index_score]
            if max_category_probability_name != current_category_name:
                individuals[individual_index_score].score = score * (1 - Fitness.PENALIZATION_COEFFICIENT)
            else:
                individuals[individual_index_score].score = score

    @staticmethod
    def calculateTFIDF(train_data_category: DataCategory) ->  None:
        vectorizer = TfidfVectorizer()
        result = vectorizer.fit_transform(train_data_category.documents)
        feature_names = vectorizer.get_feature_names()

        feature_tfidf_map = {}

        for index in set(result.nonzero()[1]):
            if result[0, index] > 0.0:
                feature_tfidf_map[feature_names[index]] = result[0, index]

        Fitness.TFIDF[train_data_category.categoryName] = feature_tfidf_map