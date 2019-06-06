from sklearn.feature_extraction.text import TfidfVectorizer
from EmailParser import DataCategory
from Log import LoggerHandler


class TFIDF:


    TFIDF_VALUES = {}

    @staticmethod
    def compute(individuals_words: dict):
        individuals_score = {}

        for category_name in individuals_words:
            individuals_score[category_name] = 0

        for category_name in individuals_words:
            for word in individuals_words[category_name]:
                if word in TFIDF.TFIDF_VALUES[category_name]:
                    individuals_score[category_name] = individuals_score[category_name] + TFIDF.TFIDF_VALUES[category_name][word]

        for category_name in individuals_score:
            individuals_score[category_name] = individuals_score[category_name] / len(individuals_words[category_name])

        return sum(individuals_score.values())/len(individuals_words)

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
        LoggerHandler.log(__name__, f"TFIDF computed for category {train_data_category.categoryName}")