from Log.LoggerHandler import LoggerHandler
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
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
        categories = [category for category in population]

        train_corpus = []
        for category in population:
            print(category)
            for individual in population[category]:
                train_corpus.append(' '.join(individual.getSelectedWords()))

        # Index for each email in each category
        labels = []
        i = 0
        for category in population:
            for _ in range(len(population[category])):
                labels.append(i)
            i = i + 1

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

        # print(train_corpus)
        text_clf.fit(train_corpus, labels)
        predicted = text_clf.predict(test_data)
        # print(Counter(test_data_labels))
        print(np.mean(predicted == test_data_labels))


