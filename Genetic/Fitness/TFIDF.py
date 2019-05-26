from sklearn.feature_extraction.text import TfidfVectorizer
from EmailParser import DataCategory
from Genetic.Components import Individual
import numpy as np

class TFIDF:


    TFIDF_VALUES = {}

    @staticmethod
    def compute(current_category_name: str, individuals_words, individuals: Individual):
        individuals_score = {}

        for category in TFIDF.TFIDF_VALUES:
            individuals_score[category] = []
            for individual_index in range(len(individuals)):
                probabilities_of_words = []
                for word in individuals_words[individual_index]:
                    if word in TFIDF.TFIDF_VALUES[category]:
                        probabilities_of_words.append(TFIDF.TFIDF_VALUES[category][word])
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
                lenExceed = individuals[individual_index_score].chromosome.lenght - Individual.MAX_INDIVIDUAL_FEATURES
                if lenExceed > 0 and TFIDF.PENALIZATION_GT_MAX_FEATURES > 0:
                    score = score / np.log(lenExceed)

                individuals[individual_index_score].score = score * (1 - TFIDF.PENALIZATION_BAD_CATEGORY)
            else:
                lenExceed = individuals[individual_index_score].chromosome.lenght - Individual.MAX_INDIVIDUAL_FEATURES
                if lenExceed > 0 and TFIDF.PENALIZATION_GT_MAX_FEATURES > 0:
                    score = score / np.log(lenExceed)

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

        TFIDF.TFIDF_VALUES[train_data_category.categoryName] = feature_tfidf_map