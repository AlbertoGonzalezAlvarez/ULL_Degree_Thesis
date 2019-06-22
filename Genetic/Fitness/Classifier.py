from Genetic.Fitness import *
from Genetic.Individual import *
from Genetic.Chromosome import *
from EmailParser.DataCategory import *
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class Classifier(FitnessFunctions):

    @staticmethod
    def evaluate(individual: CategorizedIndividual, train_data: [DataCategory]):
        test_labels = []

        for category in train_data:
            test_labels += [category.name * len(category)]

        text_clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

        chromosome = individual.chromosome
        text_clf.fit(chromosome.chromosomeDocuments(), chromosome.chromosomeCategories())
        predicted = text_clf.predict(train_data)

        score_for_category = f1_score(test_labels, predicted, average=None)

        return (sum(score_for_category) / len(individual.chromosome))