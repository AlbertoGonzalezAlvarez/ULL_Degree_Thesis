from Log.LoggerHandler import LoggerHandler
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.metrics import f1_score
from collections import Counter
import numpy as np

class Fitness():

    # def __init__(self, geneticAlg: type):
    #     self.geneticAlg = geneticAlg
    #     self.corpus = []
    #
    # @staticmethod
    # def startUp(geneticAlg: type):
    #     from Genetic.Simple_GA import Simple_GA
    #     if (type == None or not isinstance(geneticAlg, Simple_GA)):
    #         LoggerHandler.error(__name__, "Fitness function must receive a genetic algorithm.")
    #
    #     return Fitness(geneticAlg)

    @staticmethod
    def compute(population, test_data, test_data_labels ):
        # categories = [category for category in population]

        train_corpus = []
        labels = []
        i = 0

        for category in population:
            # print(category)
            for individual in population[category]:
                # print(individual.getSelectedWords())
                if ' '.join(individual.getSelectedWords()) != '':
                    train_corpus.append(' '.join(individual.getSelectedWords()))
                    labels.append(i)
            i = i + 1
            # print()

        # print(train_corpus, labels)

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])


        text_clf.fit(train_corpus, labels)
        predicted = text_clf.predict(test_data)
        # print(Counter(test_data_labels))
        score = f1_score(test_data_labels, predicted, average=None)
        # print(score[0], score[1], score[2])
        # asd = metrics.classification_report(test_data_labels, predicted, target_names = categories)
        # print(metrics.classification_report(test_data_labels, predicted, target_names = categories))
        # print(metrics.confusion_matrix(test_data_labels, predicted))

        return score
