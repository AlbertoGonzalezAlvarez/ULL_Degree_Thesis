from Genetic.Fitness import *
from Genetic.Individual import *
from EmailParser.DataCategory import *
from Genetic.Gen import *
from sklearn.feature_extraction.text import TfidfVectorizer
from Log import LoggerHandler


class TFIDF(FitnessFunctions):

    __TFIDF_VALUES__: dict = {}

    @staticmethod
    def evaluate(individual: BaseIndividual, train_data: [DataCategory]):
        TFIDF.__calculateTFIDF__(train_data)

        score_per_category: dict = {}
        for data_category in train_data:
            score_per_category[data_category.name] = 0

        for gen in BaseIndividual.chromosome:
            score_per_category[gen.category] += TFIDF.__TFIDF_VALUES__[gen.category][gen.word]

        individual.score = TFIDF.__meanTFIDF__(score_per_category)

    @staticmethod
    def __meanTFIDF__(individual: BaseIndividual, score_per_category: {str: int}):
        return sum(score_per_category.values())/len(individual.chromosome)

    @staticmethod
    def __calculateTFIDF__(train_data: [DataCategory]):

        if len(TFIDF.__TFIDF_VALUES__) == 0:
            LoggerHandler.log(__name__, f"Computing TFIDF for train data")

            for data_category in train_data:
                result = TfidfVectorizer().fit_transform(data_category.documents)
                feature_names = TfidfVectorizer().get_feature_names()

                feature_tfidf_map = {}

                for index in set(result.nonzero()[1]):
                    feature_tfidf_map[feature_names[index]] = result[0, index]

                TFIDF.__TFIDF_VALUES__[data_category.name] = feature_tfidf_map

            LoggerHandler.log(__name__, f"TFIDF computation finished!")


