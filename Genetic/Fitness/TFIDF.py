from Genetic.Fitness import *
from Genetic.Individual import *
from EmailParser.DataCategory import *
from sklearn.feature_extraction.text import TfidfVectorizer
from Log import LoggerHandler


class TFIDF(FitnessFunctions):

    __TFIDF_VALUES__: dict = {}

    @staticmethod
    def evaluate(individual: BaseIndividual, train_data: [DataCategory], weight: float, multiplier: int = 1):
        TFIDF.__calculateTFIDF__(train_data)

        score_per_category: dict = {}
        for data_category in train_data:
            score_per_category[data_category.name] = 0

        for gen in individual.chromosome.selected_gens:
            score_per_category[gen.category] += TFIDF.__TFIDF_VALUES__[gen.category][gen.word]

        individual.score += TFIDF.__meanTFIDF__(score_per_category) * multiplier * weight

    @staticmethod
    def __meanTFIDF__(score_per_category: {str: int}):
        return sum(score_per_category.values())

    @staticmethod
    def __calculateTFIDF__(train_data: [DataCategory]):

        if len(TFIDF.__TFIDF_VALUES__) == 0:
            LoggerHandler.log(__name__, f"Computing TFIDF for train data")

            for data_category in train_data:
                vectorizer = TfidfVectorizer()
                result = vectorizer.fit_transform(data_category.documents)
                feature_names = vectorizer.get_feature_names()

                feature_tfidf_map = {}

                for index in set(result.nonzero()[1]):
                    feature_tfidf_map[feature_names[index]] = result[0, index]

                max_size: int = sum(feature_tfidf_map.values())
                tfidf_map: dict = {key: feature_tfidf_map[key]/max_size/len(train_data) for key in feature_tfidf_map}

                TFIDF.__TFIDF_VALUES__[data_category.name] = tfidf_map

            LoggerHandler.log(__name__, f"TFIDF computation finished!")


